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
#from math import pi
#%% Função
def pi_markov_rej(N):
    '''
    
    Parameters
    ----------
    N : int
        Número de passos da simulação.

    Returns
    -------

    '''
    count = 0 # contador de pontos no círculo
    pi_list = [] # lista para a estimativa de pi
    n_list = [] # lista para o número de passos de medição
    rd.seed() # fixa a seed
    x, y, step = 0, 0, 1
    while step <= N:
        r1, r2 = rd.random()*0.3, rd.random()*2*np.pi # números aleatórios
        xn = x+r1*np.cos(r2)
        yn = y+r1*np.sin(r2)
        if xn>1 or xn<0 or yn>1 or yn<0: # ponto cai fora do quadrado
            continue 
        elif (xn)**2 + (yn)**2 <= 1: # ponto cai no círculo
            count += 1
            x = xn
            y = yn
            step += 1
        else: # ponto cai fora do círculo, dentro do quadrado
            x = xn
            y = yn
            step += 1
        if step % 100 == 0: # medir a cada 100 passos
            pi_list.append(count/step) # adiciona a estimativa de pi na lista
            n_list.append(step) # adiciona a contagem do passo usado na medição na lista
            print(step)
    n_list, pi_list = np.asarray(n_list), np.asarray(pi_list)
    return n_list, pi_list

def pi_markov_sr(N):
    '''
    
    Parameters
    ----------
    N : int
        Número de passos da simulação.

    Returns
    -------

    '''
    count = 0 # contador de pontos no círculo
    pi_list = [] # lista para a estimativa de pi
    n_list = [] # lista para o número de passos de medição
    rd.seed() # fixa a seed
    x, y, step = 0.5, 0.5, 1
    while step <= N:
        r1, r2 = rd.random()*0.3, rd.random()*2*np.pi # números aleatórios
        xn = x+r1*np.cos(r2)
        yn = y+r1*np.sin(r2)
        if xn>1 or xn<0 or yn>1 or yn<0: # ponto cai fora do quadrado, mas anterior está no círculo
            if (x)**2 + (y)**2 <= 1:
                step += 1
                count += 1
            else:
                step += 1
        elif xn**2 + yn**2 <= 1:
            count += 1
            x = xn
            y = yn
            step += 1
        else: # ponto cai fora do círculo, dentro do quadrado
            x = xn
            y = yn
            step += 1
        if step % 100 == 0: # medir a cada 100 passos
            pi_list.append(count/step) # adiciona a estimativa de pi na lista
            n_list.append(step) # adiciona a contagem do passo usado na medição na lista
            print(step)
    n_list, pi_list = np.asarray(n_list), np.asarray(pi_list)
    return n_list, pi_list

N = 1e6    
nr, pir = pi_markov_rej(N)
ns, pis = pi_markov_sr(N)
plt.plot(nr,pir,label='Com rejeição')
plt.plot(ns,pis,label='Sem rejeição')
plt.hlines(np.pi/4, nr[0], nr[-1], ls='--', color='darkred')
plt.ylim(0.7,0.85)
plt.xlim(nr[0],nr[-1])
num_ticks = list(plt.yticks()[0]) + [np.pi/4]
str_ticks = list(plt.yticks()[1]) + ['$\pi/4$']
plt.yticks(num_ticks,str_ticks)
plt.legend()
plt.title('Estimativa de $\pi/4$ por processo markoviano')
plt.ylabel('$n/N$')
plt.xlabel('$N$')
plt.show()
