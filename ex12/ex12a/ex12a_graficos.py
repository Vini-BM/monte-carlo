import numpy as np
import matplotlib.pyplot as plt
from glob import glob

# --------- Leitura dos dados ---------
cam_list = glob('walker*.txt') # lista de arquivos dos caminhantes
tlist, xlist, ylist, sdlist = [], [], [], []
for file in cam_list:
    t, x, y = np.loadtxt(file,unpack=True,encoding='latin1')
    sd = x**2 + y**2
    xlist.append(x)
    ylist.append(y)
    tlist.append(t)
    sdlist.append(sd)


# --------- Gráficos ---------

# Atualizar fonte do LaTeX
plt.rcParams.update({
    'font.family': 'serif',
    'mathtext.fontset': 'cm'
})

# 1 caminhante:
x, y, sd = xlist[0], ylist[0], sdlist[0] # primeiro da lista
fig, axes = plt.subplots(nrows=1,ncols=2) # subplots
fig.set_size_inches(12,6)
ax = axes[0] # gráfico da esquerda
ax.plot(x,y) # deslocamento
ax.set_title('Trajetória do caminhante')
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax = axes[1] # gráfico da direita
ax.plot(sd,color='darkred') # desvio quadrático
ax.set_title('Deslocamento quadrático da caminhada')
ax.set_xlabel('$t$')
ax.set_ylabel('$R(t)^2$')
plt.suptitle('Caminhada aleatória de um caminhante')
plt.subplots_adjust(wspace=0.35)
plt.savefig('grafico_1walker.png', dpi=1500)
plt.show()

# Todos os caminhantes:
msd = np.mean(sdlist, axis=0)
fig, axes = plt.subplots(nrows=1,ncols=2) # subplots
fig.set_size_inches(12,6)
ax = axes[0] # gráfico da esquerda
for x, y in zip(xlist,ylist):
    ax.plot(x,y)
ax.set_title('Trajetória dos caminhantes')
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax = axes[1] # gráfico da direita
ax.plot(msd,color='darkred') # desvio quadrático
# Reta:
dy = msd[-1]-msd[0]
dx = len(tlist[0])
alpha = dy/dx
yreta = tlist[0]*alpha + msd[0]
ax.plot(yreta,color='darkgreen',ls='--')
ax.set_title('Deslocamento quadrático médio das caminhadas')
ax.set_xlabel('$t$')
ax.set_ylabel('$\\overline{{R(t)}}^2$')
plt.suptitle(f'Caminhada aleatória de ${len(xlist)}$ caminhantes')
plt.subplots_adjust(wspace=0.35)
plt.savefig(f'grafico_{len(xlist)}walkers.png', dpi=1500)
plt.show()
