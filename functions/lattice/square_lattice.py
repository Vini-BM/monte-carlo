import numpy as np
import random as rd

# ---------- Criando a matriz de vizinhança ----------

def make_lattice(L):
    N = L**2 # número de sítios
    
    # ---------- MATRIZ DE VIZINHANÇA ----------
    vizinhanca = np.zeros((N,6)) # inicializa a matriz
    
    # ---------- Notação ----------
    # Sentido horário:
        # [i][0] índice
        # [i][1] direita
        # [i][2] abaixo
        # [i][3] esquerda
        # [i][4] acima
        # [i][5] ocupação

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
        
        # ---------- Ocupação ----------
        #vizinhanca[i][5] = 0 # rede começa desocupada
    
    # ---------- MATRIZ DA REDE ----------
    # Criei a matriz que representa a rede, mas ela não é necessária para a simulação
    # Deixei o código aqui caso seja preciso em outra aplicação
    #lattice_matrix = np.zeros((L,L))
    #for x in range(L):
    #    for y in range(L):
    #        lattice_matrix[y][x] = x + L*y # a matriz é transposta para reproduzir corretamente a vizinhança
    #        
    vizinhanca = vizinhanca.astype('int')
    #lattice_matrix = lattice_matrix.astype('int')
    return vizinhanca

