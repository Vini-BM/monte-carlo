import numpy as np
import random as rd
from time import time

# ---------- MATRIZ DE VIZINHANÇA ----------

def make_lattice(L):
    ''' ---------- Notação ----------
    Sentido horário:
        [i][0] índice
        [i][1] direita
        [i][2] abaixo
        [i][3] esquerda
        [i][4] acima
    '''
    # ---------- Inicialização ----------
    N = int(L**2) # número de sítios
    vizinhanca = np.zeros((N,6)) # inicializa a matriz
    
    # ---------- Loop para criar a vizinhança ----------
    for i in range(N):
    
        # ---------- Índice ----------
        vizinhanca[i][0] = i
        
        # ---------- Direita ----------
        # múltiplo de L subtraído de 1
        # ------------------------------
        if i%L == L-1: # última coluna -> ccp -> descontar L-1
            vizinhanca[i][1] = i+1-L # vai para a primeira coluna
        else: # demais colunas -> somar 1
            vizinhanca[i][1] = i+1

        # ---------- Abaixo ----------
        # índice maior ou igual do que L**2 - L
        # ------------------------------
        if i >= N-L: # última linha -> ccp -> módulo L
            vizinhanca[i][2] = i%L # vai para a primeira linha
        else: # demais linhas -> somar L
            vizinhanca[i][2] = i+L
        
        # ---------- Esquerda ----------
        #         múltiplos de L
        # ------------------------------
        if i%L == 0: # primeira coluna -> ccp -> somar L-1
            vizinhanca[i][3] = i+L-1 # vai para a última coluna
        else: # demais colunas -> descontar 1
            vizinhanca[i][3] = i-1
        
        # ---------- Acima ----------
        #     índice menor do que L
        # ------------------------------
        if i<L: # primeira linha -> ccp -> somar N-L
            vizinhanca[i][4] = i-L+N # vai para a última linha
        else: # demais linhas -> descontar L
            vizinhanca[i][4] = i-L
    
    vizinhanca = vizinhanca.astype('int')
    return vizinhanca


# ---------- Criando a matriz da rede ----------

# Criei a matriz que representa a rede, mas ela não é necessária para a simulação
# Deixei o código aqui caso seja preciso em outra aplicação

def make_lattice_matrix(L):
    lattice_matrix = np.zeros((L,L))
    for x in range(L):
        for y in range(L):
            lattice_matrix[y][x] = x + L*y # a matriz é transposta para reproduzir corretamente a vizinhança
            
    lattice_matrix = lattice_matrix.astype('int')
    return lattice_matrix


# ---------- MATRIZ DE OCUPAÇÃO ----------

def make_occupation(L,p,seed=time()):
    '''
    Cria uma matriz de ocupação a partir da densidade p.
    Gera números aleatórios e compara com p: se r<p, o sítio é ocupado.
    Ao final, devemos ter em média p*N sítios ocupados.
    '''
    N = int(L**2)
    occupation = np.zeros(N) # inicializa a matriz de ocupação com zeros
    rd.seed(seed) # fixa a seed
    for i in range(N): # loop nos sítios
        r = rd.random() # número aleatório
        if r < p: occupation[i] = 1 # sítio i fica ocupado se número aleatório for menor que a densidade
    return occupation
