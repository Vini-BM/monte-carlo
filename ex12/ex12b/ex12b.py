import numpy as np
import matplotlib.pyplot as plt
from glob import glob
import random as rd
from time import time
import sys
sys.path.insert(0, '../../functions/lattice')
from square_lattice import make_lattice
sys.path.insert(0, '../../functions/random-walker')
from random_walkers import lattice_walker

# ----- Simulação -----

# Parâmetros:
L = 20 # tamanho da rede
viz = make_lattice(L) # matriz de vizinhança, matriz da rede
num_walkers = 1000 # número de caminhantes
# Inicialização:
for i in range(num_walkers):
    seed = time()
    cam = lattice_walker(viz,seed)
    output = open(f'latticewalker_{cam.id}.dat', 'w')
    output.write('# time  x   y   site   sd\n')
    # x e y aumentam sem cota para compor o sd,
    # mas a trajetória é confinada na rede; assim,
    # usamos x_site e y_site para representar a posição
    # do caminhante na rede
    x_site, y_site = cam.site%L, cam.site//L
    output.write(f'0    {x_site}    {y_site}    {cam.site}    0 \n')
    tf = 400
    for t in range(1,tf):
        cam.move()
        sd = cam.x**2 + cam.y**2
        x_site, y_site = cam.site%L, cam.site//L
        output.write(f'{t}    {x_site}    {y_site}    {cam.site}    {sd} \n')
    output.close()
