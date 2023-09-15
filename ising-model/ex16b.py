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
        
        spins = [1 for i in range(N)] # m(0)=1
        #spins = uniform_spin(N,seed)
        energy = measure_energy(spins, lattice) # energia inicial
        mag = measure_magnetization(spins) # magnetização inicial = 1
        
        step = 1
        transient_steps = 500 # intervalo transiente

        while step < transient_steps:
            # Monte Carlo Step
            energy, spins = metropolis_mcs(energy,spins,lattice,beta)
            mag = measure_magnetization(spins)
            step += 1

        # ----- Equilíbrio -----

        spins0 = spins.copy() # spins em t=0
        mag0 = measure_magnetization(spins0) # magnetização em t=0
        step = 1
        num_steps = 1000 # intervalo em equilíbrio

        # Saída
        saida = open(f'files/indep_rand_spatial_corr_L{L}_T{T}.dat', 'w')
        saida.write('# r    C(r) \n')

        rmax = int(L/2) - 1 # distância máxima aos vizinhos
        r_list = np.arange(1,rmax+1,1) # valores de distância
        corr_list_global = [] # lista para a lista de correlações

        while step <= num_steps:
            # Monte Carlo Step
            energy, spins = metropolis_mcs(energy,spins,lattice,beta)

            # Medições independentes
            if step % 50 == 0:
                corr_list = [] # lista de C(r) para essa medida

                # Correlation measurement
                for r in r_list: # para cada distância
                    spin_sum = 0 # inicializa soma dos spins
                    for i in range(N): # para cada sítio
                        si = spins[i] # spin do sítio em questão
                        j_right, j_down = i, i # inicializar contador
                        # Recursão para alcançar o vizinho à distância r:
                        for dist in range(r): # para cada valor de distância até r
                            j_right = lattice[j_right][1] # vizinho da direita
                            j_down = lattice[j_down][2] # vizinho de baixo
                        sj_r, sj_d = spins[j_right], spins[j_down] # spin dos vizinhos
                        spin_sum += si*(sj_r+sj_d) # atualiza soma dos spins
                    spatial_corr = spin_sum/(2*N) - mag0**2 # correlação para essa distância
                    corr_list.append(spatial_corr) # adicionar C(r) na lista da medição
                corr_list_global.append(corr_list) # adicionar lista da medição de C(r) na lista global

            step += 1
        mean_corr = np.mean(corr_list_global,axis=0) # média de C(r) das diferentes medições
        for r, spatial_corr in zip(r_list, mean_corr):
            saida.write(f'{r}    {spatial_corr} \n') # escrever na saída
        saida.close()
