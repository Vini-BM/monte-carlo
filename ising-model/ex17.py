import numpy as np
import random as rd
from time import time
from ising_structure import *
import sys
sys.path.insert(0, '../functions/lattice')
from square_lattice import make_lattice

# ----- Inicialização -----
L_list = [25, 50, 75, 100]

for L in L_list:

    N = L**2
    lattice = make_lattice(L)
    T, Tmax = 2.0, 3.0 # temperaturas
    spins = [1 for i in range(N)] # m(0) = 1
    seed = time()
    rd.seed(seed)
    saida = open(f'files/chi_mag_L{L}_{seed}.dat', 'w')
    saida.write('# T    chi(T)    m(T) \n')

    while T <= Tmax:
        beta = 1/T
        mag_list = []
        if T > 2.1 and T < 2.4:
            dt = 0.01
        else:
            dt = 0.1

        # ------ Transiente -----
        energy = measure_energy(spins, lattice)
        mag = measure_magnetization(spins)
        step = 1
        transient_steps = 300
        while step <= transient_steps:
            # Monte Carlo Step
            energy, spins = metropolis_mcs(energy,spins,lattice,beta)
            step += 1

        # ----- Equilíbrio -----
        step = 1
        num_steps = 10000
        while step <= num_steps:
            # Monte Carlo Step
            energy, spins = metropolis_mcs(energy,spins,lattice,beta)
            if step % 50 == 0:
                mag = measure_magnetization(spins)
                mag_list.append(mag)
            step += 1

        # ----- Saída -----
        magnetization = np.mean(mag_list)
        chi = measure_chi(N, T, mag_list)
        saida.write(f'{T:.4f}    {chi}    {magnetization} \n')
        T += dt
        T = round(T, 4)
        print(T)

    saida.close()