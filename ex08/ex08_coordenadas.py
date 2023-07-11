import matplotlib.pyplot as plt
import numpy as np
from glob import glob
from math import pi

# Fonte para os gráficos
plt.rcParams.update({
    'font.family': 'serif',
	'mathtext.fontset': 'cm'
})

rej_files = glob('sim_rej_*') # lista de arquivos com rejeição
sem_files = glob('sim_sem_*') # lista de arquivos sem rejeição

nr1, pir1, xr1, yr1 = np.loadtxt(rej_files[0],unpack=True)
nr2, pir2, xr2, yr2 = np.loadtxt(rej_files[1],unpack=True)
ns1, pis1, xs1, ys1 = np.loadtxt(sem_files[0],unpack=True)
ns2, pis2, xs2, ys2 = np.loadtxt(sem_files[1],unpack=True)

# Histogramas
fig, axes = plt.subplots(nrows=2,ncols=2) # define subplots
rej_color = 'blueviolet' # cor para histogramas com rejeição
sem_color = 'tomato' # cor para histogramas sem rejeição
bins = 25 # núemro de bins

ax = axes[0,0] # superior esquerdo
ax.hist(xr1,bins=bins,color=rej_color) # rejeição 1
ax.set_title('Com rejeição')
ax.set_xlim(0,1)

ax = axes[1,0] # inferior esquerdo
ax.hist(xr2,bins=bins,color=rej_color) # rejeição 2
ax.set_xlim(0,1)

ax = axes[0,1] # superior direito
ax.hist(xs1,bins=bins,color=sem_color) # sem rejeição 1
ax.set_title('Sem rejeição')
ax.set_xlim(0,1)

ax = axes[1,1] # inferior direito
ax.hist(xs2,bins=bins,color=sem_color) # sem rejeição 2
ax.set_xlim(0,1)

fig.suptitle('Distribuição da coordenada $x$ nos métodos com e sem rejeição') # título geral
fig.supxlabel('$x$')
fig.supylabel('Contagem')

plt.savefig('hist_coordenada_ex08.png', dpi=1500)
plt.show()
