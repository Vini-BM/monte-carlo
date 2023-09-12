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
seed = 289 # seed
rd.seed(seed)

for L in L_list:
    N = L**2
    lattice = make_lattice(L)
    for T in T_list:
        beta = 1/T

        # ----- Condição inicial -----
        spins = [1 for i in range(N)]
        energy = measure_energy(spins, lattice)
        mag = measure_magnetization(spins)

        # ----- Simulação -----
        num_steps = 10000

        # Saída
        saida = open(f'files/indep_metropolis_L{L}_T{T}.dat', 'w')
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
            if step%50==0:
                saida.write(f'{step}  {energy/N}  {mag} \n')        
            step += 1
        saida.close()
