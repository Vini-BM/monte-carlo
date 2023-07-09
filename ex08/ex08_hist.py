import matplotlib.pyplot as plt
import numpy as np
import random as rd
from time import time

#%% Função
def pi_markov_rej(N,seed):
    '''
    Parameters
    ----------
    N : int
    	    Número de passos de contagem da simulação
    seed : float
	    Seed para a simulação
	
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
    x, y, step = 0.5, 0.5, 0
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
    return n_list, pi_list, x_list, y_list

def pi_markov_sr(N,seed):
    '''
    Parameters
    ----------
    N : int
        Número de passos de contagem da simulação
    seed : float
        Seed para a simulação

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
    x, y, step = 0.5, 0.5, 0
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
    return n_list, pi_list, x_list, y_list

# Média de amostras
pot = 5
N = int(10**pot)
file_rej = 'media_pi_rej_10{}.txt'.format(pot)
file_sem = 'media_pi_sem_10{}.txt'.format(pot)
saida_rej = open(file_rej,'a')
saida_rej.write('# Média da estimativa final de pi pelo método com rejeição após {} passos\n'.format(N))
saida_rej.write('# amostra    seed    pi/4\n')
saida_sem = open(file_sem,'a')
saida_sem.write('# Média da estimativa final de pi pelo método sem rejeição após {} passos\n'.format(N))
saida_sem.write('# amostra    seed    pi/4\n')
for i in range(1000): # 1000 amostras diferentes
    seed = time()
    nr, pir, xr, yr = pi_markov_rej(N,seed) # rejeição
    saida_rej.write('{}    {}    {}\n'.format(i,seed,pir[-1]))
    ns, pis, xs, ys = pi_markov_sr(N,seed) # sem rejeição
    saida_sem.write('{}    {}    {}\n'.format(i,seed,pis[-1]))
saida_rej.close()
saida_sem.close()

