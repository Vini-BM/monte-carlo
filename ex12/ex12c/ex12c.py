import numpy as np
import matplotlib.pyplot as plt
from glob import glob
from random import randint, choice
import sys
sys.path.insert(0, '../ex12b')
from ex12b import lattice_walker, make_lattice

class saw_walker(lattice_walker):
    def saw_move(self):
        self.rede[self.site][5] = 1
        neighbors = [self.rede[self.site][i] for i in range(1,5)]
        options = []
        stop = False
        for neighbor in neighbors:
            if self.rede[neighbor][5] == 0:
                options.append(neighbor)
        try:
            newsite = choice(options) # nova posição é o vizinho na direção sorteada
            self.rede[newsite][5] = 1
            self.site, self.x, self.y = newsite, newsite%self.L, newsite//self.L
        except IndexError:
            stop = True
        return stop

L = 20
lattice = make_lattice(L)
num_walkers = 100
# Inicialização:
camlist = [saw_walker(i,lattice) for i in range(num_walkers)]
for cam in camlist:
    output = open(f'sawwalker{cam.id:02}.txt', 'w')
    output.write(f'# self avoiding walk em matriz {L}x{L} \n')
    output.write('# tempo  x   y   sítio \n')
    site0, x0, y0 = cam.site, cam.x, cam.y
    output.write(f'0    {x0}    {y0}    {site0} \n')
    tf = 1000
    for t in range(1,tf):
        stop = cam.saw_move()
        if stop:
            continue
        output.write(f'{t}    {cam.x}    {cam.y}    {cam.site} \n')
    output.close()
    for j in range(len(lattice)):
        lattice[j][5] = False
