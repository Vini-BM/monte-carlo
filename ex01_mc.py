#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 18 11:05:33 2023

@author: vinibaynem
"""
import matplotlib.pyplot as plt
import random as rd
import numpy as np

# Define amostras
n1 = 100
n2 = 100
# A presença de uma bolinha no índice i é indicada por 1
amostra1 = [1 for i in range(n1)]
amostra2 = [1 for i in range(n2)]

# Função para realizar a simulação
def troca(amostra, tf):
    n = len(amostra)
    amostra = np.asarray(amostra)
    rd.seed()
    t = 0
    na = []
    while t <= tf: # O loop está dentro da função ter uma seed fixa
        index = int(n*rd.random())
        amostra[index] *= -1 # Índice da bolinha trocada é multiplicado por -1
        # Para o total de bolinhas: trocar os valores negativos por 0 e somar o array
        na.append(np.sum(np.where(amostra > 0, amostra, 0)))
        t += 1
    return na

# Função analítica para o problema
def analitico(n,t):
    return n/2 + n/2*(1-2/n)**t

# Simulação
tf = 500
na1 = troca(amostra1, tf)
na2 = troca(amostra2, tf)
tlist = np.arange(0, tf, step=1)
funcao = analitico(n1, tlist)

# Gráfico
plt.plot(na1, label='Amostra 1')
plt.plot(na2, label='Amostra 2')
plt.plot(funcao, label='Resultado analítico', color='red')
plt.legend()
plt.xlabel('Tempo')
plt.ylabel('$N_A$')
plt.title('Bolinhas na caixa A em função do tempo')
plt.savefig('grafico_ex1.png',dpi=2000)
plt.show()