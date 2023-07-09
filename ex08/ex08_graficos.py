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

# aqui eu poderia ter feito um loop e automatizado,
# mas como são apenas duas amostras para cada método,
# decidi fazer manualmente
nr1, pir1, xr1, yr1 = np.loadtxt(rej_files[0],unpack=True)
nr2, pir2, xr2, yr2 = np.loadtxt(rej_files[1],unpack=True)
ns1, pis1, xs1, ys1 = np.loadtxt(sem_files[0],unpack=True)
ns2, pis2, xs2, ys2 = np.loadtxt(sem_files[1],unpack=True)


# Gráfico
plt.plot(nr1,pir1,label='Com rejeição',color='darkorange')
plt.plot(nr2,pir2,label='Com rejeição',color='blue')
plt.plot(ns1,pis1,label='Sem rejeição',color='red')
plt.plot(ns2,pis2,label='Sem rejeição',color='green')
plt.hlines(np.pi/4, nr1[0], nr1[-1], ls='--', color='black')
plt.ylim(0.7,0.85)
plt.xlim(nr1[0],nr1[-1])

# Para adicionar um tick em pi/4:
locs, labels = plt.yticks()
newlocs = np.append(locs,pi/4)
newlabels = np.around(np.copy(locs),3)
newlabels = np.append(newlabels,'$\pi/4$') # Se simplesmente adicionar a label em latex, as outras labels vão sumir
plt.yticks(ticks=newlocs,labels=newlabels)

plt.legend()
plt.title('Estimativa de $\pi/4$ por processo markoviano')
plt.ylabel('$n/N$')
plt.xlabel('$N$')
plt.savefig('grafico_ex08.png', dpi=1500)
plt.show()


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
