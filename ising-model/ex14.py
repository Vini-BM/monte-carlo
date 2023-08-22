import numpy as np
from time import time
from os.path import isfile
from ising_structure import uniform_spin, measure_energy, measure_magnetization
import sys
sys.path.insert(0, '../functions/lattice')
from square_lattice import make_lattice

L_list = [5, 10, 50, 100]

for L in L_list: # escolhe L
    N = L**2 # número de sítios
    lattice = make_lattice(L) # cria a rede
    output_name = f'files/uniformising_en_mag_L{L}.dat'
    if isfile(output_name):
        output_file = open(output_name, 'a')
    else:
        output_file = open(output_name, 'w')
        output_file.write('# energy/N    magnetization    seed \n')
    for repeat in range(5000): # número de vezes que roda o programa
        seed = time() # fixa a seed
        spins = uniform_spin(N,seed) # cria spins
        energy = measure_energy(spins,lattice) # mede energia
        magnetization = measure_magnetization(spins) # mede magnetização
        output_file.write(f'{energy/N}    {magnetization}    {seed} \n')
    output_file.close()
