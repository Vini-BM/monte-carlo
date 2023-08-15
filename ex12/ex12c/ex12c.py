import numpy as np
import matplotlib.pyplot as plt
from glob import glob
import random as rd
from time import time
import sys
sys.path.insert(0, '../../functions/random-walker')
from random_walkers import saw_walker
sys.path.insert(0, '../../functions/lattice')
from square_lattice import make_lattice

L = 20
lattice = make_lattice(L)
num_walkers = 10000
# Inicialização:
for i in range(num_walkers):
    seed = time()
    cam = saw_walker(lattice,seed)
    output = open(f'sawwalker_{cam.id}.dat', 'w')
    output.write('# tempo  x   y   site    sd \n')
    output.write(f'0    {cam.x}    {cam.y}    {cam.site}    0 \n')
    tf = 1000
    for t in range(1,tf):
        stop = cam.move()
        if stop:
            continue
        sd = cam.x**2 + cam.y**2
        output.write(f'{t}    {cam.x}    {cam.y}    {cam.site}    {sd} \n')
    output.close()
    for j in range(len(lattice)):
        cam.occupation[j] = 0
