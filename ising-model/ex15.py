import numpy as np
import random as rd
from ising_structure import *
from ising_metropolis import metropolis_flip
import sys
sys.path.insert(0, '../functions/lattice')
from square_lattice import make_lattice

# Inicialização
L = 50
N = L**2
lattice = make_lattice(L)

# Condição inicial
spins = uniform_spin(N)


