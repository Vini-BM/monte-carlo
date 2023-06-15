#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 11:06:41 2023

@author: vinibaynem
"""
#%%
import matplotlib.pyplot as plt
import numpy as np
import random as rd
from scipy.optimize import curve_fit
from math import pi
#%%
def pi_agulhas(N):
    '''
    Estima o valor de pi pelo problema das agulhas de Buffon.
    Realiza medidas a cada 100 passos.
    Retorna o valor de pi em função do número de passos usados na medição.
    É um programa circular pois utiliza internamente o valor de pi para gerar
    os números aleatórios, mas foge do escopo utilizar outros métodos. O valor
    utilizado é o da biblioteca math, de maior precisão que o valor do numpy.

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
    count = 0 # contador de agulhas que cruzam uma linha
    pi_list = [] # lista para a estimativa de pi
    n_list = [] # lista para o número de passos de medição
    for i in range(1,int(N)+1): # int(N) para garantir que será tratado como inteiro
        r1 = rd.random() * pi # número aleatório de 0 a pi
        r2 = rd.random() # número aleatório de 0 a 1
        if r2 < np.sin(r1): count += 1 # agulha cruza uma linha
        if count > 0 and i % 100 == 0:
            # duas condições para a medição:
            # a. não medir enquanto não houver um ponto dentro do círculo, para evitar divisão por zero
            # b. medir a cada 100 passos
            pi_list.append(2*i/count) # adiciona a estimativa de pi na lista
            n_list.append(i) # adiciona a contagem do passo usado na medição na lista
    n_list, pi_list = np.asarray(n_list), np.asarray(pi_list)
    return n_list, pi_list
#%% Simulação
runs = 10
N = 1e6
pi_list = []
for i in range(runs):
    n_, pi_ = pi_agulhas(N)
    pi_list.append(pi_)
#print(len(pi_list))
#pi_list = np.asarray(pi_list)
n_list, pi_list = n_, np.mean(pi_list,axis=0)
#%% Gráfico para a estimativa de pi
plt.figure(figsize=(10,6))
plt.plot(n_list,pi_list, label='Estimativa')
plt.xlim(n_list[0], n_list[-1])
plt.ylim(3.138,3.152)
plt.hlines(y=pi, xmin=n_list[0], xmax=n_list[-1], ls='--', color='darkred', label='Valor real')
extratick = [pi]
plt.yticks(list(plt.yticks()[0])+extratick)
plt.legend()
plt.xlabel('$N \ (10^7)$')
plt.ylabel('Valor para $\pi$')
plt.title('Estimativa de $\pi$ em função do número $N$ de agulhas lançadas')
#plt.savefig('grafico_pi_ex05.png',dpi=1500)
plt.show()
#%% Fitting no erro
# Aqui é feito um fitting linear com o logaritmo do erro para encontrar a
# dependência exponencial do erro com o número de passos
erro = np.abs(pi_list-pi)
n_log, erro_log = np.log(n_list), np.log(erro)
def reta(x,a,b): # fitting 
    return a*x + b
lim = 20
popt, pcov = curve_fit(reta, n_log[lim:], erro_log[lim:]) # parâmetros, matriz de covariância
a, b = popt # coeficiente angular, coeficiente linear
fit = reta(n_log[lim:],a,b) # valores calculados a partir da função com os parâmetros encontrados (para o gráfico)
print('Coeficiente angular: {}'.format(a))
#%% Gráfico para o erro
plt.figure(figsize=(8,4))
plt.plot(n_log, erro_log)
plt.plot(n_log[lim:], fit)
plt.xlim(n_log[0], n_log[-1])
plt.xlabel('$\ln N$')
plt.ylabel('$\ln |2N/n - \pi|$')
plt.title('Erro na estimativa')
#plt.savefig('grafico_erro_ex05.png',dpi=1500)
plt.show()