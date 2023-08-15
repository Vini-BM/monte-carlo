import numpy as np
import random as rd

# ---------- Caminhante aleatório ----------
class walker():
    def __init__(self,walkerseed,step=1):
        self.id, self.passo = walkerseed, step # identifica o caminhante pela seed e define o tamanho do passo (1 por padrão)
        self.x, self.y = 0, 0 # posição inicial
        rd.seed(self.id)
    def move(self):
        # direita: x+=1 -- 1
        # abaio: y-=1 -- 2
        # esquerda: x-=1 -- 3
        # acima: y+=1 -- 4
        r = rd.randint(1,4)
        if r == 1:
            self.x += self.passo
        elif r == 2:
            self.y -= self.passo
        elif r == 3:
            self.x -= self.passo
        else:
            self.y += self.passo

# ---------- Caminhante aleatório na rede ----------
class lattice_walker():
    def __init__(self,lattice,walkerseed):
        self.id, self.rede = walkerseed, lattice # identidade do caminhante (seed) e matriz onde ele caminha
        rd.seed(self.id)
        self.N = len(lattice)
        self.L = int(np.sqrt(self.N)) # tamanho da rede
        #self.occupation = np.zeros(self.N) # matriz de ocupação
        self.site = rd.randint(0,self.L**2-1) # sítio inicial (randint é inclusivo nos extremos, então o limite deve ser L**2 - 1)
        # x é o módulo da divisão do sítio por L e y é o resultado inteiro da divisão do sítio por L (pela construção da matriz)
        self.x, self.y = 0, 0
    def move(self):
        r = rd.randint(1,4) # escolha da direção (1-direita, 2-abaixo, 3-esquerda, 4-acima)
        newsite = self.rede[self.site][r] # nova posição é o vizinho na direção sorteada
        self.site = newsite
        if r == 1:
            self.x += 1
        elif r == 2:
            self.y += 1
        elif r == 3:
            self.x -= 1
        elif r == 4:
            self.y -= 1

# ---------- Caminhante aleatório do tipo SAW ----------
class saw_walker(lattice_walker):
    def __init__(self,lattice,walkerseed):
        lattice_walker.__init__(self,lattice,walkerseed)
        self.occupation = np.zeros(self.N) # matriz de ocupação
    def move(self):
        self.occupation[self.site] = 1
        neighbors = [self.rede[self.site][i] for i in range(1,4)]
        options = []
        stop = False
        for neighbor in neighbors:
            if self.occupation[neighbor] == 0:
                options.append(neighbor)
            else:
                options.append(self.site)
        if all(sites == self.site for sites in options):
            stop = True
        newsite = rd.choice(options) # nova posição é o vizinho na direção sorteada ou o caminhante continua na mesma posição
        self.occupation[newsite] = 1
        r = np.argwhere(self.rede[self.site] == newsite)[0]
        if r == 1:
            self.x += 1
        elif r == 2:
            self.y += 1
        elif r == 3:
            self.x -= 1
        elif r == 4:
            self.y -= 1
        self.site = newsite
        return stop
