import numpy as np
import matplotlib.pyplot as plt
from glob import glob
from random import randint

# Definindo caminhante:

class walker():
    x, y = 0, 0
    def __init__(self,ident,step=1):
        self.passo, self.id = step, ident
    def move(self):
        # direita: x+=1 -- 0
        # abaio: y-=1 -- 1
        # esquerda: x-=1 -- 2
        # acima: y+=1 -- 3
        r = randint(0,3)
        if r == 0:
            self.x += self.passo
        elif r == 1:
            self.y -= self.passo
        elif r == 2:
            self.x -= self.passo
        else:
            self.y += self.passo

# Criando a matriz de vizinhança:

def make_lattice(L):
    N = L**2 # número de sítios
    
    # ---------- MATRIZ DE VIZINHANÇA ----------
    vizinhanca = np.zeros((N,5)) # inicializa a matriz
    
    # ---------- Notação ----------
    # Sentido horário:
        # [i][0] índice
        # [i][1] direita
        # [i][2] abaixo
        # [i][3] esquerda
        # [i][4] acima

    # ---------- Loop para criar a vizinhança ----------
    for i in range(N):
    
        # ---------- Índice ----------
        vizinhanca[i][0] = i
        
        # ---------- Direita ----------
        # múltiplo de L subtraído de 1
        # ------------------------------
        if i%L == L-1: # última coluna -> ccp -> descontar L-1
            vizinhanca[i][1] = i+1-L # vai para a primeira coluna
        else: # demais colunas -> somar 1
            vizinhanca[i][1] = i+1

        # ---------- Abaixo ----------
        # índice maior ou igual do que L**2 - L
        # ------------------------------
        if i >= N-L: # última linha -> ccp -> módulo L
            vizinhanca[i][2] = i%L # vai para a primeira linha
        else: # demais linhas -> somar L
            vizinhanca[i][2] = i+L
        
        # ---------- Esquerda ----------
        #         múltiplos de L
        # ------------------------------
        if i%L == 0: # primeira coluna -> ccp -> somar L-1
            vizinhanca[i][3] = i+L-1 # vai para a última coluna
        else: # demais colunas -> descontar 1
            vizinhanca[i][3] = i-1
        
        # ---------- Acima ----------
        #     índice menor do que L
        # ------------------------------
        if i<L: # primeira linha -> ccp -> somar N-L
            vizinhanca[i][4] = i-L+N # vai para a última linha
        else: # demais linhas -> descontar L
            vizinhanca[i][4] = i-L
    
    # ---------- MATRIZ DA REDE ----------
    lattice_matrix = np.zeros((L,L))
    for x in range(L):
        for y in range(L):
            lattice_matrix[y][x] = x + L*y
            
    vizinhanca = vizinhanca.astype('int')
    return vizinhanca, lattice_matrix

l = 6
viz, lat = make_lattice(l)
#viz = viz.astype('int')
#print(viz)
#print(lat)
#print(lat[2][3])

start = randint(0,l**2)
index = np.argwhere(lat == start)[0]
x, y = index[0], index[1]
#print(start)
xlist, ylist = [x], [y]
pos = start
for t in range(30):
    r = randint(1,4)
    newpos = viz[pos][r]
    x, y = np.argwhere(lat == newpos)[0]
    xlist.append(x)
    ylist.append(y)
    pos = newpos
print(xlist)