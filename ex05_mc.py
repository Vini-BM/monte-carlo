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
from time import time
#%% Função
def pi_agulhas(N,seed=''):
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
    seed : float
        Seed da simulação. Se não especificada, é utilizado o timestamp do sistema.
        
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
    rd.seed(seed) # fixa a seed da simulação
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
runs = 100
N = 1e6
pi_list = []
filename = 'ex05.log'
with open(filename,'w') as saida: # arquivo para escrever os prints
    saida.write('Exercício 5\n')
for i in range(runs):
    seed = time()
    n_, pi_ = pi_agulhas(N,seed)
    pi_list.append(pi_)
    print(i) # teste do programa
    with open(filename,'a') as saida:
        saida.write('Simulação {}, seed = {}, pi = {}\n'.format(i,seed,pi_[-1])) # controle das simulações
n_list, pi_list = n_, np.mean(pi_list,axis=0)
with open(filename,'a') as saida:
	print('Estimativa final: pi = {}\n'.format(pi_list[-1]), file=saida) # estimativa final
#%% Gráfico para a estimativa de pi
plt.plot(n_list,pi_list, label='Estimativa')
plt.xlim(n_list[0], n_list[-1])
plt.ylim(3.138,3.148)
extra = [pi]
plt.yticks(list(plt.yticks()[0])+extra)
plt.hlines(y=pi, xmin=n_list[0], xmax=n_list[-1], ls='--', color='darkred', label='Valor real')
plt.legend()
plt.xlabel('$N$')
plt.ylabel('Valor para $\pi$')
plt.title('Estimativa de $\pi$ em função do número $N$ de agulhas lançadas')
plt.savefig('grafico_ex05_pi.png',dpi=1500)
plt.show()
#%% Fitting no erro
# Aqui é feito um fitting linear com o logaritmo do erro para encontrar a
# dependência exponencial do erro com o número de passos
erro = np.abs(pi_list-pi)
n_log, erro_log = np.log(n_list), np.log(erro)
def reta(x,a,b): # fitting 
    return a*x + b
lim = 20 # limite inferior do fit para desconsiderar flutuações, escolhido no olho
popt, pcov = curve_fit(reta, n_log[lim:], erro_log[lim:]) # parâmetros, matriz de covariância
a, b = popt # coeficiente angular, coeficiente linear
fit = reta(n_log[lim:],a,b) # valores calculados a partir da função com os parâmetros encontrados (para o gráfico)
with open(filename,'a') as saida:
    saida.write('\nFit do erro na escala logarítmica:\n')
    saida.write('Coeficiente angular: {}\n'.format(a))
    saida.write('Coeficiente linear: {}\n'.format(b))
#%% Gráfico para o erro
plt.plot(n_log, erro_log)
plt.plot(n_log[lim:], fit, label='Ajuste linear\n(Coeficiente angular = {:.3f})'.format(a))
plt.xlim(n_log[0], n_log[-1])
plt.legend()
plt.xlabel('$\ln N$')
plt.ylabel('$\ln |2N/n - \pi|$')
plt.title('Erro na estimativa')
plt.savefig('grafico_ex05_erro.png',dpi=1500)
plt.show()