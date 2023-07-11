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
from time import time

#%% Função
def pi_markov_rej(N,seed,file=True):
    '''
    Parameters
    ----------
    N : int
    	    Número de passos de contagem da simulação
    seed : float
	    Seed para a simulação
    file : boolean
	    Decide se escreve a saída em um arquivo ou não
	
    Returns
    -------
    n_list : array
        Número de passos de contagem organizados em array
    pi_list : array
        Estimativa de pi em função do número de passos
    x_list : list
        Coordenada x a cada passo
    y_list : list
        Coordenada y a cada passo
    '''
    count = 0 # contador de pontos no círculo
    pi_list = [] # lista para a estimativa de pi
    n_list = [] # lista para o número de passos de medição
    rd.seed(seed) # fixa a seed
    x, y, step = 0.5, 0.5, 0 # passo inicia no zero
    x_list, y_list = [x], [y]
    while step <= N:
        r1, r2 = rd.random()*0.3, rd.random()*2*np.pi # números aleatórios
        xn = x+r1*np.cos(r2)
        yn = y+r1*np.sin(r2)
        if 0<=xn<=1 and 0<=yn<=1: # ponto cai dentro do quadrado
            step += 1
            if xn**2 + yn**2 <= 1: # ponto cai dentro do círculo
                count += 1
            x = xn
            y = yn
        else: # ponto cai fora do quadrado
            continue
        #if step % 100 == 0: # medir a cada 100 passos
        x_list.append(x)
        y_list.append(y)
        pi_list.append(count/step) # adiciona a estimativa de pi na lista
        n_list.append(step) # adiciona a contagem do passo usado na medição na lista
        print(step)
    n_list, pi_list = np.asarray(n_list), np.asarray(pi_list)
    # Escrever em arquivos
    if file:
        with open('sim_rej_{}.txt'.format(seed),'w') as saida:
            saida.write('# Simulação com rejeição com seed {}\n'.format(seed))
            saida.write('# n    pi/4    x    y\n')
            for i in range(int(len(n_list)/100)):
                saida.write('{}    {}     {}     {}\n'.format(n_list[i*100],pi_list[i*100],x_list[i*100],y_list[i*100]))
    return n_list, pi_list, x_list, y_list

def pi_markov_sr(N,seed,file=True):
    '''
    Parameters
    ----------
    N : int
        Número de passos de contagem da simulação
    seed : float
        Seed para a simulação
    file : boolean
        Decide se escreve a saída em um arquivo ou não

    Returns
    -------
    n_list : array
        Número de passos de contagem organizados em array
    pi_list : array
        Estimativa de pi em função do número de passos
    x_list : list
        Coordenada x a cada passo
    y_list : list
        Coordenada y a cada passo
    '''
    count = 0 # contador de pontos no círculo
    pi_list = [] # lista para a estimativa de pi
    n_list = [] # lista para o número de passos de medição
    rd.seed(seed) # fixa a seed
    x, y, step = 0.5, 0.5, 0 # passo inicia no zero
    x_list, y_list = [x], [y]
    while step <= N:
        r1, r2 = rd.random()*0.3, rd.random()*2*np.pi # números aleatórios
        xn = x+r1*np.cos(r2)
        yn = y+r1*np.sin(r2)
        if 0<=xn<=1 and 0<=yn<=1: # ponto cai dentro do quadrado
            step += 1
            if xn**2 + yn**2 <= 1: # ponto cai dentro do círculo
                count += 1
            x = xn
            y = yn
        else: # ponto cai fora do quadrado
            step += 1
            if (x)**2 + (y)**2 <= 1:
                count += 1 # ponto anterior está no círculo
        #if step % 100 == 0: # medir a cada 100 passos
        x_list.append(x)
        y_list.append(y)
        pi_list.append(count/step) # adiciona a estimativa de pi na lista
        n_list.append(step) # adiciona a contagem do passo usado na medição na lista
        print(step)
    n_list, pi_list = np.asarray(n_list), np.asarray(pi_list)
    # Escrever em arquivos
    if file:
        with open('sim_sem_{}.txt'.format(seed),'w') as saida:
            saida.write('# Simulação sem rejeição com seed {}\n'.format(seed))
            saida.write('# n    pi/4    x    y\n')
            for i in range(int(len(n_list)/100)):
                saida.write('{}    {}     {}     {}\n'.format(n_list[i*100],pi_list[i*100],x_list[i*100],y_list[i*100]))
    return n_list, pi_list, x_list, y_list


# Simulação
N = 1e6
n = 10
for i in range(n):
    seed = time()
    nr, pir, xr, yr = pi_markov_rej(N,seed) # rejeição
    ns, pis, xs, ys = pi_markov_sr(N,seed) # sem rejeição

