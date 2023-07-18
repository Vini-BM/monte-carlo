import matplotlib.pyplot as plt
import numpy as np
from glob import glob

# --------- Leitura dos dados ---------
cam_list = glob('latticewalker*.txt') # lista de arquivos dos caminhantes
tlist, xlist, ylist, sitelist, sdlist = [], [], [], [], []
for file in cam_list:
    t, x, y, site = np.loadtxt(file,unpack=True)
    sd = x**2 + y**2
    xlist.append(x)
    ylist.append(y)
    sitelist.append(site)
    tlist.append(t)
    sdlist.append(sd)

# --------- Gráficos ---------

# Atualizar fonte do LaTeX
plt.rcParams.update({
    'font.family': 'serif',
    'mathtext.fontset': 'cm'
})

# Todos os caminhantes:
msd = np.mean(sdlist, axis=0)
fig, axes = plt.subplots(nrows=1,ncols=2) # subplots
fig.set_size_inches(24,8)
ax = axes[0] # gráfico da esquerda
for x, y in zip(xlist,ylist):
    ax.plot(x,y)
ax.set_title('Trajetória dos caminhantes')
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')

ax = axes[1] # gráfico da direita
ax.plot(msd,color='darkred') # desvio quadrático
# Reta:
#dy = msd[-1]-msd[0]
#dx = len(tlist[0])
#alpha = dy/dx
#yreta = tlist[0]*alpha + msd[0]
#ax.plot(yreta,color='darkgreen',ls='--')
ax.set_title('Deslocamento quadrático médio das caminhadas')
ax.set_xlabel('$t$')
ax.set_ylabel('$\\overline{{R(t)}}^2$')
#plt.xlim(2000)
plt.suptitle(f'Caminhada aleatória de ${len(xlist)}$ caminhantes')
plt.subplots_adjust(wspace=0.35)
#plt.savefig(f'grafico_{len(xlist)}latticewalkers.png', dpi=1500)
plt.show()