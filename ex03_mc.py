#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 30 10:41:30 2023

@author: vinibaynem
"""
import matplotlib.pyplot as plt
import random as rd
import numpy as np
from time import time
#%% Amostra
n = 100
amostra = [1 for i in range(n)] # bolinha presente indicada por 1 no índice correspondente
#%% Função da simulação
def troca(amostra, tf, seed=''): # seed como parâmetro opcional, caso não especificada o programa utiliza o valor padrão (timestamp)
    n = len(amostra) # tamanho da amostra
    p_n = [0 for i in range(n+1)] # lista para a probabilidade, 101 elementos para considerar 0 e 100 (para evitar erros no código)
    amostra = np.asarray(amostra) # transforma a lista em array para realizar as operações do numpy
    rd.seed(seed) # utiliza a seed especificada
    t = 0 # inicia o tempo de simulação
    m = 0 # contador
    na_list = [] # lista para o número de bolinhas em A
    while t <= tf:
        index = int(n*rd.random()) # sorteia um número aleatório de 0 a 99
        amostra[index] = (amostra[index]-1)*(-1) # troca de bolinha representada por subtração de 1 e multiplicação por -1
        soma = np.sum(amostra) # soma dos elementos = Na
        na_list.append(soma) # adiciona Na do instante correspondente à lista
        if t % 101 == 0: # 101 pelo problema da paridade
            m += 1
            p_n[soma] += 1 # contagem da ocupação do estado correspondente
        t += 1
    p_n = np.asarray(p_n)/m # normalização
    return na_list, amostra, p_n # retorna o número de bolas em A, a amostra após a simulação e a dens. de probabilidade
#%% Arquivo
n_bin, p_bin = np.loadtxt('bin100.dat', unpack=True)
n_bin, p_bin = np.insert(n_bin, 0, 0.0), np.insert(p_bin, 0, 0.0) # adiciona a prob. para 0 no arquivo para os eixos coincidirem
n_bin, p_bin = np.insert(n_bin, 100, 0.0), np.insert(p_bin, 100, 0.0) # mesmo para 100, mas não faz diferença no gráfico
#%% Simulaçao no regime transiente
seed = time() # fixar a seed com o timestamp de antes da simulação, para não mudar na passagem do sistema transiente ao estacionário
tf = 500
na, amostra_t, p_nt = troca(amostra, tf, seed)
#%% Simulação no regime estacionário - continua a partir da mesma amostra, mesma seed
teq = 10100000 # múltiplo de 101 para não desperdiçar medidas
na_eq, amostra_eq, p_na = troca(amostra_t, teq, seed)
#%% Grafico de probabilidades no regime estacionário
plt.scatter(range(len(p_na)), p_na, color='blue', s=12, label=r'$p(N_A)$')
plt.plot(p_bin, color='darkred', label='Probabilidade binomial')
plt.legend()
plt.xlabel(r'$n$')
plt.ylabel('Densidade de probabilidade')
plt.title('Probabilidade de ocupação dos valores do sistema')
plt.xlim(30,70)
plt.savefig('grafico_ex3.png',dpi=2000)
plt.show()