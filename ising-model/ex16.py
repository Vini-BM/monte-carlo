import numpy as np
import random as rd
from time import time
from ising_structure import *
import sys
sys.path.insert(0, '../functions/lattice')
from square_lattice import make_lattice

# ----- Inicialização -----
T_list = [1, 2.27, 3]
L_list = [50, 100]

for L in L_list:
    N = L**2
    lattice = make_lattice(L)
    for T in T_list:
        beta = 1/T

        # ------ Transiente -----
        seed = time()
        rd.seed(seed)
        
        spins = uniform_spin(N,seed)
        energy = measure_energy(spins, lattice)
        mag = measure_magnetization(spins)
        
        step = 1
        transient_steps = 300
        while step < transient_steps:
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
            step += 1

        # ----- Equilíbrio -----

        spins0 = spins.copy() # spins em t=0
        mag0 = measure_magnetization(spins0) # magnetização em t=0
        temporal_corr_list = [0] # lista para a correlação temporal

        step = 1
        num_steps = 1000

        # Saída
        saida = open(f'files/temporal_corr_L{L}_T{T}_{seed}.dat', 'w')
        saida.write(f'# mcs    C(t) \n')
        saida.write(f'0    0 \n')

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
            # Correlation measurement
            spin_sum = 0
            #mag = measure_magnetization(spins)
            for s in range(N):
                spin_sum += spins[s]*spins0[s]
            temporal_corr = spin_sum/N - mag0**2
            temporal_corr_list.append(temporal_corr)
            saida.write(f'{step}    {temporal_corr} \n')
            step += 1

        saida.close()
