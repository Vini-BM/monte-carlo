#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 11:41:01 2023

@author: vinibaynem
"""
#%%
import matplotlib.pyplot as plt
import numpy as np
import random as rd
from math import pi
#%% Função
def pi_circulo(N):
    '''

    
    Parameters
    ----------
    N : int
        Número de passos da simulação.

    Returns
    -------
    n_list : array
        Contagem de passos de medição.
    pi_list : array
        Estimativa de pi para o correspondente número de passos.

    '''
    count = 0 # contador de pontos no círculo
    pi_list = [] # lista para a estimativa de pi
    n_list = [] # lista para o número de passos de medição
    rd.seed() # fixa a seed
    for i in range(1,int(N)+1): # int(N) para garantir que será tratado como inteiro
        r1, r2 = rd.random()*0.3, rd.random()*2*pi # números aleatórios
        if 
        if r1**2 + r2**2 <= 1: count.append(r2) # ponto cai no círculo
        if count > 0 and i % 100 == 0:
            # duas condições para a medição:
            # a. não medir enquanto não houver um ponto dentro do círculo, para evitar divisão por zero
            # b. medir a cada 100 passos
            pi_list.append(4*count/i) # adiciona a estimativa de pi na lista
            n_list.append(i) # adiciona a contagem do passo usado na medição na lista
    n_list, pi_list = np.asarray(n_list), np.asarray(pi_list)
    return n_list, pi_list