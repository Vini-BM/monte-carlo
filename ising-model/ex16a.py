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
        
        spins = [1 for i in range(N)]
        energy = measure_energy(spins, lattice)
        mag = measure_magnetization(spins)
        
        step = 1
        transient_steps = 300
        while step < transient_steps:
            # Monte Carlo Step
            energy, spins = metropolis_mcs(energy,spins,lattice,beta)
            mag = measure_magnetization(spins)
            step += 1

        # ----- Equilíbrio -----

        spins0 = spins.copy() # spins em t=0
        mag0 = measure_magnetization(spins0) # magnetização em t=0

        step = 1
        num_steps = 1000

        # Saída
        saida = open(f'files/uni_temporal_corr_L{L}_T{T}_{seed}.dat', 'w')
        saida.write(f'# mcs    C(t) \n')
        saida.write(f'0    {1/N - mag0} \n')

        while step < num_steps:
            # Monte Carlo Step
            energy, spins = metropolis_mcs(energy,spins,lattice,beta)
            spin_sum = 0
            #mag = measure_magnetization(spins)
            for s in range(N):
                spin_sum += spins[s]*spins0[s]
            temporal_corr = spin_sum/N - mag0**2
            saida.write(f'{step}    {temporal_corr} \n')
            step += 1

        saida.close()
