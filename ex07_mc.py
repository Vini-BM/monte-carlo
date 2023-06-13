# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 19:36:18 2023

@author: Vinicius
"""

#%%
import matplotlib.pyplot as plt
import numpy as np
import random as rd
#%% Funções
def funcao(x):
    return np.sin(1/x)**2

def integracao(f,N,xlim):
    '''
    Integração por Monte Carlo pelo método de amostragem média.
    A integral da função é estimada pela área média abaixo da curva.

    Parameters
    ----------
    f : function
        Função a ser integrada
    N : int
        Número de passos.
    xlim : array ou lista de 2 elementos
        Limites de integração.

    Returns
    -------
    integral : float
        Integral da função f entre os limites dados em xlim.
    '''
    integral = 0 # inicia o contador
    x_int = abs(xlim[1]-xlim[0]) # largura do intervalo
    for i in range(int(N)): # int(N) para garantir que N seja tratado como inteiro
        xr = rd.random()*x_int+xlim[0] # número aleatório dentro do intervalo de integração
        fr = f(xr) # valor da função f aplicada no número aleatório gerado
        integral += fr/N * x_int # aumenta o contador pela 'área' média
    return integral
#%% Valores da função
xlim = [0,1]
#%% Simulação
N = 1000000
integral = integracao(funcao,N,xlim)
print(integral)