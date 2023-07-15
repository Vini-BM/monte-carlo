import numpy as np
import matplotlib.pyplot as plt
from random import randint

# Caminhada aleatória 2D sem superfície

#vizinhança = []
#direita, abaixo, esquerda, acima = [], [], [], []

# Definindo caminhante:
class walker():
    x, y = 0, 0
    def __init__(self,ident,step=1):
        self.passo, self.id = step, ident
    def move(self):
        # direita: x+=1 -- 0
        # abaio: y-=1 -- 1
        # esquerda: x-=1 -- 2
        # acima: y+=1 -- 3
        r = randint(0,3)
        if r == 0:
            self.x += self.passo
        elif r == 1:
            self.y -= self.passo
        elif r == 2:
            self.x -= self.passo
        else:
            self.y += self.passo

# Simulação:
walkerlist = list(walker(i) for i in range(100))
xlist_g, ylist_g, sd_g = [], [], []
tf = 10000
for cam in walkerlist:
    file = open(f'walker{cam.id:02}.txt', 'w')
    file.write('# caminhante aleatório 2D \n')
    file.write('# tempo    x    y \n')
    xlist, ylist, sd = [cam.x], [cam.y], [cam.x**2 + cam.y**2]
    for i in range(tf):
        cam.move()
        xlist.append(cam.x)
        ylist.append(cam.y)
        sd.append(cam.x**2 + cam.y**2)
        file.write(f'{i}    {cam.x}    {cam.y} \n')
    xlist_g.append(xlist)
    ylist_g.append(ylist)
    sd_g.append(sd)
    file.close()

