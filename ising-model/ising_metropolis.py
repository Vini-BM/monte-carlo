import numpy as np
import random as rd
from ising_structure import measure_energy

def metropolis_flip(spins, lattice, beta):
    '''
    Troca um spin individual no modelo de Ising pelo algoritmo de Metropolis.
    A probabilidade de aceite é dada por e^{-delta_e/(KbT)}, se delta_e > 0,
    e 1, se delta_e < 0.
    Retorna os spins após aceitar ou não a troca.
    '''
    N = len(spins) # número de sítios
    initial_spins = spins.copy() # spins iniciais
    initial_energy = measure_energy(initial_spins,lattice) # energia inicial
    k = rd.randint(0,N-1) # sítio aleatório
    spins[k] *= -1 # troca de spin
    final_energy = measure_energy(spins,lattice) # energia final
    delta_e = final_energy - initial_energy # variação de energia
    if delta_e < 0:
        return spins # aceita a troca com probabilidade 1
    else:
        p = np.exp(-beta*delta_e) # probabilidade de aceite
        r = rd.random() # número aleatório
        if r > p:
            return spins # aceita a troca com probabilidade p
        else:
            return old_spins # rejeita a troca
