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
#from math import pi

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
    x, y, step = 0.5, 0.5, 1
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
        with open('ex08_rej_{}.txt'.format(seed),'w') as saida:
            saida.write('# Simulação com rejeição com seed {}\n'.format(seed))
            saida.write('# n    pi/4    x    y\n')
            for i in range(len(n_list)):
               saida.write('{}    {}    {}    {}\n'.format(n_list[i],pi_list[i],x_list[i],y_list[i]))
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
    x, y, step = 0.5, 0.5, 1
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
        with open('ex08_sem_{}.txt'.format(seed),'w') as saida:
            saida.write('# Simulação sem rejeição com seed {}\n'.format(seed))
            saida.write('# n    pi/4    x    y\n')
            for i in range(len(n_list)):
                saida.write('{}    {}     {}     {}\n'.format(n_list[i],pi_list[i],x_list[i],y_list[i]))
    return n_list, pi_list, x_list, y_list


# Simulação
N = 1e6
## Amostra 1
seed1 = time()
nr1, pir1, xr1, yr1 = pi_markov_rej(N,seed1) # rejeição
ns1, pis1, xs1, ys1 = pi_markov_sr(N,seed1) # sem rejeição
## Amostra 2
seed2 = time()
nr2, pir2, xr2, yr2 = pi_markov_rej(N,seed2) # rejeição
ns2, pis2, xs2, ys2 = pi_markov_sr(N,seed2) # sem rejeição

# Gráfico
plt.plot(nr1,pir1,label='Com rejeição ({})'.format(seed1),color='orange')
plt.plot(nr2,pir2,label='Com rejeição ({})'.format(seed2),color='blue')
plt.plot(ns1,pis1,label='Sem rejeição ({})'.format(seed1),color='red')
plt.plot(ns2,pis2,label='Sem rejeição ({})'.format(seed2),color='green')
plt.hlines(np.pi/4, nr1[0], nr1[-1], ls='--', color='darkred')
num_ticks = list(plt.yticks()[0]) + [np.pi/4]
str_ticks = list(plt.yticks()[1]) + ['$\pi/4$']
plt.yticks(ticks=num_ticks,labels=str_ticks)
plt.ylim(0.7,0.85)
plt.xlim(nr1[0],nr1[-1])
plt.legend()
plt.title('Estimativa de $\pi/4$ por processo markoviano')
plt.ylabel('$n/N$')
plt.xlabel('$N$')
plt.savefig('grafico_ex08.png', dpi=1500)
plt.show()

# Histograma com rejeição
plt.hist(xr1,bins=100,label='Seed = {}'.format(seed1),color='orange')
plt.hist(xr2,bins=100,label='Seed = {}'.format(seed2),color='blue')
plt.xlabel('Coordenada x')
plt.ylabel('Contagem')
plt.title('Contagem da coordenada $x$ com rejeição')
plt.legend()
plt.savefig('hist_rej_ex08.png', dpi=1500)
plt.show()

# Histograma sem rejeição
plt.hist(xs1,bins=100,label='Seed = {}'.format(seed1),color='red')
plt.hist(xs2,bins=100,label='Seed = {}'.format(seed2),color='green')
plt.xlabel('Coordenada x')
plt.ylabel('Contagem')
plt.title('Contagem da coordenada $x$ sem rejeição')
plt.legend()
plt.savefig('hist_sr_ex08.png', dpi=1500)
plt.show()

# Média de amostras
file_rej = 'ex08_media_pi_rej.txt'
file_sem = 'ex08_media_pi_sem.txt'
saida_rej = open(file_rej,'w')
saida_rej.write('# Média da estimativa de pi pelo método com rejeição após {} passos\n'.format(N))
saida_rej.write('# amostra    seed    pi\n')
saida_sem = open(file_sem,'w')
saida_sem.write('# Média da estimativa de pi pelo método sem rejeição após {} passos\n'.format(N))
saida_sem.write('# amostra    seed    pi\n')
for i in range(100):
    seed = time()
    nr, pir, xr, yr = pi_markov_rej(N,seed,file=False) # rejeição
    saida_rej.write('{}    {}    {}'.format(i,seed,pir[-1]))
    ns, pis, xs, ys = pi_markov_sr(N,seed,file=False) # sem rejeição
    saida_sem.write('{}    {}    {}'.format(i,seed,pis[-1]))
saida_rej.close()
saida_sem.close()

