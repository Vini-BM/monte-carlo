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
walkerlist = list(walker(i) for i in range(10))
xlist_g, ylist_g = [], []
tf = 1000
for cam in walkerlist:
    xlist, ylist = [cam.x], [cam.y]
    for i in range(tf):
        cam.move()
        xlist.append(cam.x)
        ylist.append(cam.y)
    xlist_g.append(xlist)
    ylist_g.append(ylist)
# Gráficos
#limx, limy = max(np.abs(xlist)), max(np.abs(ylist))
for xlist, ylist in zip(xlist_g,ylist_g):
    plt.plot(xlist,ylist)
#plt.xlim(-limx,limx)
#plt.ylim(-limy,limy)
plt.show()
