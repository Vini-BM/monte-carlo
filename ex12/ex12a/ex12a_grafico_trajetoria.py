import numpy as np
import matplotlib.pyplot as plt
from glob import glob

# --------- Leitura dos dados ---------
cam_list = glob('walker*.dat') # lista de arquivos dos caminhantes
tlist, xlist, ylist, sdlist = [], [], [], []
for file in cam_list:
    t, x, y, sd = np.loadtxt(file,unpack=True,encoding='latin1')
    xlist.append(x)
    ylist.append(y)
    tlist.append(t)
    sdlist.append(sd)

# --------- Gráfico ---------

# Atualizar fonte do LaTeX
plt.rcParams.update({
    'font.family': 'serif',
    'mathtext.fontset': 'cm'
})

fig, axes = plt.subplots(nrows=1,ncols=2) # subplots
fig.set_size_inches(12,6)
# 1 caminhante:
x, y, sd = xlist[0], ylist[0], sdlist[0] # primeiro da lista
ax = axes[0] # gráfico da esquerda
ax.plot(x,y)
ax.set_title('Caminhada aleatória de um caminhante')
# Todos os caminhantes:
ax = axes[1] # gráfico da direita
for x, y in zip(xlist,ylist):
    ax.plot(x,y)
ax.set_title(f'Caminhada aleatória de ${len(xlist)}$ caminhantes')
fig.supxlabel('$x$')
fig.supylabel('$y$')
plt.savefig(f'trajetoria_{len(xlist)}walkers.png', dpi=1500)
plt.show()
