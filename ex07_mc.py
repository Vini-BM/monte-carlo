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
    integral_r : float
        Integral da função calculada pela razão dos pontos.
    integral_am : float
        Integral da função calculada pela amostragem média.
    '''
    integral_r, integral_am = 0, 0 # inicia os contadores
    x_int = abs(xlim[1]-xlim[0]) # largura do intervalo
    rd.seed(seed)
    for i in range(int(N)): # int(N) para garantir que N seja tratado como inteiro
        xr = rd.random()*x_int+xlim[0] # número aleatório dentro do intervalo de integração
        yr = rd.random()*ymax # número aleatório dentro do intervalo de valores assumidos por f
        fr = f(xr) # valor da função f aplicada no número aleatório gerado
        if yr <= fr: integral_r += 1/N * ymax * x_int # aumenta o contador da razão
        integral_am += fr/N * x_int # aumenta o contador da amostragem média
    return integral_r, integral_am
#%% Valores da função
xlim = [0,1] # intervalo de integração
ymax = 1 # valor máximo do seno
#%% Simulação: valor da integral em função do tempo
N = 100000 # número de passos
list_r, list_am, n_list = [], [], [] # listas para as integrais e para o número de passos
seed = time() # fixa a seed
for i in range(100,N+1,100):
    # Calcula (do zero) a integral usando i passos
    # Começa com 100 passos e vai até N de 100 em 100
    int_razao, int_am = integracao(funcao,i,xlim,ymax,seed)
    list_r.append(int_razao)
    list_am.append(int_am)
    n_list.append(i)
#%% Valores
print('Razão entre pontos: I={}'.format(list_r[-1]))
print('Amostragem média: I={}'.format(list_am[-1]))
#%% Gráfico
plt.plot(n_list,list_r,label='Razão entre pontos: $I = 0.6730$',color='darkgreen')
plt.plot(n_list,list_am,label='Amostragem média: $I = 0.6736$',color='darkred')
plt.xlim(n_list[0],n_list[-1])
plt.ylim(0.66,0.69)
plt.legend()
plt.xlabel('Número de passos')
plt.ylabel('Valor estimado')
plt.title('Integração numérica em função do número de passos')
plt.savefig('grafico_ex07.png', dpi=1500)
plt.show()