import numpy as np
import matplotlib.pyplot as plt
from time import time
import sys
sys.path.insert(0, '../../functions/random-walker')
from random_walkers import walker

# Caminhada aleatória 2D sem superfície

# Simulação:
num_walkers = 1000 # número de caminhantes
tf = 1000 # número de passos
for i in range(num_walkers):
    seed = time() # fixa a seed de cada caminhante
    cam = walker(seed)
    file = open(f'walker_{cam.id}.dat', 'w')
    file.write('# time    x    y    sd \n')
    file.write('0    0    0    0 \n')
    for t in range(1,tf):
        cam.move()
        sd = cam.x**2 + cam.y**2
        file.write(f'{t}    {cam.x}    {cam.y}    {sd} \n')
    file.close()
