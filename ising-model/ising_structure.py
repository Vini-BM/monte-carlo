import numpy as np
import random as rd
from time import time

def uniform_spin(N,seed=time()):
    '''
    Gera uma configuração aleatória de spins por amostragem direta.
    N: número de sítios da rede
    seed: seed do gerador (por padrão, é o timestamp do sistema)
    '''
    rd.seed(seed) # fixa a seed
    spins = [] # inicializa a lista de spins
    for i in range(N):
        r = rd.randint(0,1) # 1/2 de probabilidade para cada estado
        s = 2*r - 1 # valores aleatórios se tornam -1 ou 1
        spins.append(s)
    return spins

def measure_energy(spins,lattice,J=1):
    '''
    Mede a energia do modelo de Ising sem campo externo a partir do valor dos spins e da matriz de vizinhança
    spins: array com o spin de cada sítio da rede
    lattice: matriz de vizinhança da rede
    J: interação entre sítios (por padrão J=1)
    '''
    sum_spin = 0 # inicializa soma
    N = len(spins) # número de sítios
    for i in range(N):
        sum_spin # inicializa soma sobre i
        spin_i = spins[i] # spin do sítio i
        neighbor_spins = [lattice[i][1], lattice[i][2]] # vizinhos da direita e de baixo do sítio i (evitar redundâncias)
        for j in neighbor_spins: # loop sobre vizinhos
            spin_j = spins[j] # spin do sítio j
            sum_spin += spin_i * spin_j # aumenta contador da soma sobre i
    energy = -J * sum_spin # divide por dois para remover os termos repetidos
    return energy
    
def measure_magnetization(spins):
    '''
    Mede a magnetização do modelo de Ising a partir do valor dos spins da rede.
    '''
    sum_spin = 0
    N = len(spins)
    for spin in spins:
        sum_spin += spin
    magnetization = sum_spin/N
    return magnetization

