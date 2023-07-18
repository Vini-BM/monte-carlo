import numpy as np
import matplotlib.pyplot as plt
from glob import glob
from random import randint
from ex12b import lattice_walker, make_lattice

class saw_walker(lattice_walker):
    def saw_move(self)
        r = randint(1,4) # escolha da direção (1-direita, 2-abaixo, 3-esquerda, 4-acima)
        newsite = self.rede[self.site][r] # nova posição é o vizinho na direção sorteada
        if not self.rede[newsite][5]:
            self.site = newsite
        
        self.x, self.y = self.site%self.L, self.site//self.L