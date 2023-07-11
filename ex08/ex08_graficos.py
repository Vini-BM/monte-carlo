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

rej_final, sem_final = [], []
for rej, sem in zip(rej_files, sem_files):
    nr, pir, xr, yr = np.loadtxt(rej,unpack=True)
    rej_final.append(pir[-1])
    ns, pis, xs, ys = np.loadtxt(sem,unpack=True)
    sem_final.append(pis[-1])
    # Gráfico
    plt.plot(nr,pir,ls='--')
    plt.plot(ns,pis)
plt.hlines(np.pi/4, nr[0], nr[-1], ls=':', color='black')
plt.ylim(0.7,0.85)
plt.xlim(nr[0],nr[-1])
# Para adicionar um tick em pi/4:
locs, labels = plt.yticks()
newlocs = np.append(locs,pi/4)
newlabels = np.around(np.copy(locs),3)
newlabels = np.append(newlabels,'$\pi/4$') # Se simplesmente adicionar a label em latex, as outras labels vão sumir
plt.yticks(ticks=newlocs,labels=newlabels)
#plt.legend()
plt.text(700000, 0.82, '--- Com rejeição', fontsize='large')
plt.text(700000, 0.77, '$\\emdash$ Sem rejeição', fontsize='large')
plt.title('Estimativa de $\pi/4$ por processo markoviano')
plt.ylabel('$n/N$')
plt.xlabel('$N$')
plt.savefig('grafico_ex08.png', dpi=1500)
plt.show()

rej_final = 4*np.asarray(rej_final)
rej_media = np.mean(rej_final)
rej_dp = np.std(rej_final)/np.sqrt(len(rej_final)-1)
sem_final = 4*np.asarray(sem_final)
sem_media = np.mean(sem_final)
sem_dp = np.std(sem_final)/np.sqrt(len(sem_final)-1)
print('Média com rejeição: {} +- {}'.format(rej_media, rej_dp))
print('Média sem rejeição: {} +- {}'.format(sem_media, sem_dp))