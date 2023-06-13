# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 19:20:50 2023

@author: Vinicius
"""

#%%
import matplotlib.pyplot as plt
import numpy as np
import random as rd
from math import pi
#%%
def pi_circulo(N):
    '''
    Estima o valor de pi por Monte Carlo pelo problema do círculo inscrito.
    Realiza medidas a cada 100 passos.
    Retorna o valor de pi em função do número de passos usados na medição.
    
    Parameters
    ----------
    N : int
        Número de passos da simulação.

    Returns
    -------
    n_list : array
        Array com a contagem de passos de medição.
    pi_list : array
        Array com a estimativa de pi para o correspondente número de passos.

    '''
    count = [] # contador de pontos no círculo
    pi_list = [] # lista para a estimativa de pi
    n_list = [] # lista para o número de passos de medição
    rd.seed()
    for i in range(1,int(N)+1): # int(N) para garantir que será tratado como inteiro
        r1, r2 = rd.random(), rd.random() # números aleatórios
        if r1**2 + r2**2 <= 1: count.append(r2) # ponto cai no círculo
        if len(count) != 0 and i % 100 == 0:
            # duas condições para a medição:
            # a. não medir enquanto não houver um ponto dentro do círculo, para evitar divisão por zero
            # b. medir a cada 100 passos
            pi_list.append(4*len(count)/i) # adiciona a estimativa de pi na lista
            n_list.append(i) # adiciona a contagem do passo usado na medição na lista
    n_list, pi_list = np.asarray(n_list), np.asarray(pi_list)
    return n_list, pi_list
#%% Simulação
runs = 100
N = 1e6
pi_list = []
for i in range(runs):
    n, pi_ = pi_circulo(N)
    pi_list.append(pi_)
#%%
n_list = n
pi_list = np.mean(pi_list,axis=0)
#%% Gráfico
plt.figure(figsize=(10,6))
plt.plot(n_list, pi_list, label='Estimativa')
plt.hlines(y=pi, xmin=n_list[0], xmax=n_list[-1], ls='--', color='darkred', label='Valor real')
plt.xlim(n_list[0], n_list[-1])
plt.ylim(3.14,3.143)
extratick = [pi]
plt.yticks(list(plt.yticks()[0])+extratick)
plt.xlabel('$N$')
plt.ylabel('Estimativa para $\pi$')
plt.legend()
plt.title('Estimativa para $\pi$ pelo método do círculo')
plt.show()