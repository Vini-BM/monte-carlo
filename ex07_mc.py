# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 19:36:18 2023

@author: Vinicius
"""

#%% Imports
import numpy as np
import random as rd
import matplotlib.pyplot as plt
from time import time
#%% Funções
def funcao(x):
    return np.sin(1/x)**2

def integracao(f,N,xlim,ymax,seed=''):
    '''
    Integração por Monte Carlo pela razão de pontos abaixo e fora da curva
    e pelo método de amostragem média.
    A integral é calculada dentro do intervalo especificado.
    
    Parameters
    ----------
    f : function
        Função a ser integrada
    N : int
        Número de passos.
    xlim : array ou lista de 2 elementos
        Limites de integração.
    ymax: float
        Valor máximo da função no intervalo.
    seed: int
        Seed da simulação. Se não especificada, é utilizado o timestamp do sistema.

    Returns
    -------
    integral_d: float
        Integral da função calculada pela amostragem direta.
    integral_am : float
        Integral da função calculada pela amostragem média.
    '''
    integral_d, integral_am = 0, 0 # inicia os contadores
    x_int = abs(xlim[1]-xlim[0]) # largura do intervalo
    rd.seed(seed)
    for i in range(int(N)): # int(N) para garantir que N seja tratado como inteiro
        xr = rd.random()*x_int+xlim[0] # número aleatório dentro do intervalo de integração
        yr = rd.random()*ymax # número aleatório dentro do intervalo de valores assumidos por f
        fr = f(xr) # valor da função f aplicada no número aleatório gerado
        if yr <= fr: integral_d += 1/N * ymax * x_int # aumenta o contador da amostragem direta
        integral_am += fr/N * x_int # aumenta o contador da amostragem média
    return integral_d, integral_am
#%% Valores da função
xlim = [0,1] # intervalo de integração
ymax = 1 # valor máximo do seno
#%% Simulação: valor da integral em função do tempo
runs = 10 # numero de simulaçoes
N = 100000 # número de passos
list_d_runs, list_am_runs = [], [] # listas para as integrais e para o número de passos
for i in range(runs):
    seed = time() # fixa a seed para a simulaçao
    list_d, list_am, n_list = [], [], []
    for j in range(100,N+1,100):
        # Calcula (do zero) a integral usando i passos
        # Começa com 100 passos e vai até N de 100 em 100
        int_d, int_am = integracao(funcao,j,xlim,ymax,seed)
        list_d.append(int_d)
        list_am.append(int_am)
        n_list.append(j)
    list_d_runs.append(list_d)
    list_am_runs.append(list_am)
#%% Valores medios
list_d_media = np.mean(list_d_runs,axis=0)
list_am_media = np.mean(list_am_runs,axis=0)
#%% Valores
print('Amostragem direta: I={}'.format(list_d_media[-1]))
print('Amostragem média: I={}'.format(list_am_media[-1]))
#%% Gráfico
plt.plot(n_list,list_d,label='Amostragem direta: $I = {:.4f}$'.format(list_d_media[-1]),color='darkgreen')
plt.plot(n_list,list_am,label='Amostragem média: $I = {:.4f}$'.format(list_am_media[-1]),color='darkred')
plt.xlim(n_list[0],n_list[-1])
plt.ylim(0.66,0.69)
plt.legend()
plt.xlabel('Número de passos')
plt.ylabel('Valor estimado')
plt.title('Integração numérica em função do número de passos')
plt.savefig('grafico_ex07.png', dpi=1500)
plt.show()