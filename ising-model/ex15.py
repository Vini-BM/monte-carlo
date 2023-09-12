import numpy as np
import random as rd
from time import time
from ising_structure import *
import sys
sys.path.insert(0, '../functions/lattice')
from square_lattice import make_lattice

# ----- Inicialização -----
L_list = [50,100] # tamanhos do sistema
T_list = [1,2,3,5] # temperaturas do sistema
homogeneous_list = [False, True]
seed = 150 # seed
rd.seed(seed)

for L in L_list:
    N = L**2
    lattice = make_lattice(L)
    for T in T_list:
        beta = 1/T
        for homogeneous in homogeneous_list:
            # ----- Condição inicial -----
            if homogeneous: # condição inicial m(0) = 1
                spins = [1 for i in range(N)]
                hom_label = 'hom'
            else: # condição inicial aleatória
                spins = uniform_spin(N, seed=seed)
                hom_label = 'rand'
            energy = measure_energy(spins, lattice)
            mag = measure_magnetization(spins)

            # ----- Simulação -----
            num_steps = 1000

            # Saída
            saida = open(f'files/metropolis_L{L}_T{T}_{hom_label}.dat', 'w')
            saida.write(f'# mcs  energy  magnetization \n')
            saida.write(f'0  {energy/N}  {mag} \n')

            # Loop
            step = 1
            while step < num_steps:
                # Monte Carlo Step
                for i in range(N):
                    delta_e = delta_energy(i, spins, lattice)
                    if delta_e <= 0: # aceita a troca
                        spins[i] *= -1
                        energy += delta_e
                    else:
                        p = np.exp(-beta*delta_e) # probabilidade de aceite
                        r = rd.random() # número aleatório
                        if r < p: # aceita a troca
                            spins[i] *= -1
                            energy += delta_e
                mag = measure_magnetization(spins)
                saida.write(f'{step}  {energy/N}  {mag} \n')        
                step += 1
            saida.close()
