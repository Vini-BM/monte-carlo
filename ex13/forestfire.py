import numpy as np
import random as rd
import sys
from time import time
sys.path.insert(0, '../functions/lattice')
from square_lattice import make_lattice, make_occupation

# ----- Parâmetros -----
L_list = [50, 100, 150] # tamanho da rede
p_list = np.arange(0.3,0.91,0.01) # densidade de ocupação

# ----- Loop em L -----
for L in L_list:
    seed = time() # seed
    
    # ----- Criar a rede, definir ocupação -----
    neighborhood = make_lattice(L) # matriz de vizinhança
    out = open(f'forestfire_L{L}_{seed}.dat','w') # arquivo de saída
    out.write('# p    t \n')

    # ----- Loop em p -----
    for p in p_list:

        # ----- Matriz de ocupação -----
        occupation = make_occupation(L,p,seed)

        # ----- Matriz do fogo -----
        fire = np.zeros(L**2) # 1 se a árvore está queimando, 0 se não
        # No início, colocamos fogo nas árvores da primeira linha: 0 <= i <= L-1
        for i in range(L): # loop nos sítios da primeira linha
            if occupation[i] == 1: # checa se o sítio i tem árvore
                fire[i] = 1 # coloca fogo na árvore
        
        # ----- Loop na rede -----
        t = 1
        burning = True
        while burning:

            # Colocar fogo
            forest = np.nonzero(occupation)[0]
            for tree in forest:
                neighbor_trees = neighborhood[tree]
                for neighbor in neighbor_trees:
                    if occupation[neighbor] == 1 and fire[tree] == 1:
                        fire[neighbor] = 1
            
            # Incrementar tempo
            t += 1
            
            # Condição de parada
            burning_trees = np.nonzero(fire)[0]
            available = []
            for tree in burning_trees:
                neighbor_trees = neighborhood[tree]
                for neighbor in neighbor_trees:
                    if occupation[neighbor] == 1 and fire[neighbor] == 0:
                        available.append(neighbor)
            if len(available) == 0:
                burning = False
        
        # ----- Saída -----
        out.write(f'{p}    {t} \n')

    out.close()
