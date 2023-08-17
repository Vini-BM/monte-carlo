import numpy as np
import random as rd
from time import time
import sys
sys.path.insert(0, '../lattice')
from square_lattice import make_lattice

def define_spin(N,seed=time()):
    rd.seed(seed)
    spins = []
    for i in range(N):
        r = rd.randint(0,1) # 1/2 de probabilidade para cada estado
        s = 2*r - 1 # valores aleatórios se tornam -1 ou 1
        spins.append(s)
    return spins

def energy(spins,lattice,J=1):
    sum_spin = 0
    N = len(spins)
    for i in range(N):
        sum_spin_i = 0
        spin_i = spins[i]
        neighbor_spins = lattice[i]
        for j in neighbor_spins:
            spin_j = spins[j]
            sum_spin_i += spin_i * spin_j
        sum_spin += sum_spin_i
    sum_spin *= -J/2
    return sum_spin

L = 5
N = L**2

lattice = make_lattice(L)
spins = define_spin(N)
energy = energy(spins,lattice)
print(energy)

