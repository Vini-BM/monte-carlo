#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 30 10:41:30 2023

@author: vinibaynem
"""
#%% Imports
import matplotlib.pyplot as plt
import random as rd
import numpy as np
from time import time
#%% Função da simulação
def troca(amostra, tf, seed=''):
    '''
    Simulação das urnas de Ehrenfest pelo método de Monte Carlo.
    A cada instante, sorteia uma bolinha numerada de 0 a 99 e troca-a de urna.
    O número de bolinhas na urna A é contado a cada instante, a e probabilidade
    de encontrar esse valor é medida a cada 101 passos.
    

    Parameters
    ----------
    amostra : array/lista
        Estado da urna A antes do processo de troca. A presença da bolinha
        no índice i é indicada por 1, e a ausência, por 0.
    tf : int
        Número de passos (tempo discretizado) da simulação
    seed : float (opcional)
        Seed para o gerador de números aleatórios. Caso não especificada, será
        usado o valor padrão da função (timestamp do sistema).
        
    Returns
    -------
    na_list : array
        Número total de bolinhas na urna A para cada instante da simulação.
    amostra : array
        Estado final da urna A.
    p_n : array
        Distribuição de probabilidade para o número total de bolinhas na urna.
    '''
    n = len(amostra) # tamanho da amostra
    p_n = [0 for i in range(n+1)] # lista para a probabilidade, 101 elementos para considerar 0 e 100 (para evitar erros no código)
    amostra = np.asarray(amostra) # transforma a lista em array para realizar as operações do numpy
    rd.seed(seed) # utiliza a seed especificada
    t = 0 # inicia o tempo de simulação
    m = 0 # contador
    na_list = [] # lista para o número de bolinhas em A
    while t <= tf:
        index = int(n*rd.random()) # sorteia um número aleatório de 0 a 99
        amostra[index] = 1-amostra[index] # troca de bolinha
        soma = np.sum(amostra) # soma dos elementos = Na
        na_list.append(soma) # adiciona Na do instante correspondente à lista
        if t % 101 == 0: # 101 pelo problema da paridade
            m += 1
            p_n[soma] += 1 # contagem da ocupação do estado correspondente
        t += 1
    p_n = np.asarray(p_n)/m # normalização da distribuição de probabilidade
    return na_list, amostra, p_n
#%% Amostra
n = 100
amostra = [1 for i in range(n)] # bolinha presente indicada por 1 no índice correspondente
#%% Arquivo
# Aqui adicionei 0 para a probabilidade de encontrar 0 ou 100 bolinhas, para 
# que o número de valores (101) coincidisse com os da simulação.
# Não editei o arquivo bin100.dat para que não houvesse inconsistência ao rodar
# em outras máquinas com o arquivo original
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
#%% Gráfico de probabilidades no regime estacionário
plt.scatter(range(len(p_na)), p_na, color='blue', s=12, label=r'$p(N_A)$')
plt.plot(p_bin, color='darkred', label='Probabilidade binomial')
plt.legend()
plt.xlabel(r'$N_A$')
plt.ylabel('Distribuição de probabilidade')
plt.title('Probabilidade de ocupação dos valores do sistema')
plt.xlim(30,70)
plt.savefig('grafico_ex03.png',dpi=1500)
plt.show()
