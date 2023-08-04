import numpy as np
import matplotlib.pyplot as plt
from glob import glob
from random import randint, choice
import sys
sys.path.insert(0, '../ex12b')
from ex12b import lattice_walker, make_lattice

class saw_walker(lattice_walker):
    def __init__(self,ident,lattice):
        lattice_walker.__init__(self,ident,lattice)
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
        newsite = choice(options) # nova posição é o vizinho na direção sorteada ou o caminhante continua na mesma posição
        self.occupation[newsite] = 1
        self.site, self.x, self.y = newsite, abs(newsite%self.L - self.x0), abs(newsite//self.L - self.y0)
        return stop
        

if __name__ == '__main__':
    L = 20
    lattice = make_lattice(L)
    num_walkers = 1000
    # Inicialização:
    camlist = [saw_walker(i,lattice) for i in range(num_walkers)]
    for cam in camlist:
        output = open(f'sawwalker{cam.id:03}.txt', 'w')
        output.write(f'# self avoiding walk em matriz {L}x{L} \n')
        output.write('# tempo  x   y   sítio \n')
        site0, x0, y0 = cam.site, cam.x, cam.y
        output.write(f'0    {x0}    {y0}    {site0} \n')
        tf = 1000
        for t in range(1,tf):
            stop = cam.move()
            if stop:
                continue
            output.write(f'{t}    {cam.x}    {cam.y}    {cam.site} \n')
        output.close()
        for j in range(len(lattice)):
            cam.occupation[j] = 0
