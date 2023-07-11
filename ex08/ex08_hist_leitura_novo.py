import numpy as np
import matplotlib.pyplot as plt
from math import pi

file_rej = 'media_pi_rej_105.txt'
file_sem = 'media_pi_sem_105.txt'

amostra_r, seed_r, pir = np.loadtxt(file_rej,unpack=True,encoding='latin1')
amostra_s, seed_s, pis = np.loadtxt(file_sem,unpack=True,encoding='latin1')

pir *= 4
pis *= 4


media_r = np.mean(pir)
media_s = np.mean(pis)
dp_r = np.sqrt(np.var(pir)/(len(pir)-1))
dp_s = np.sqrt(np.var(pis)/(len(pis)-1))
xr = np.arange(np.min(pir),np.max(pir),step=0.00001)
xs = np.arange(np.min(pis),np.max(pis),step=0.00001)

print('Rejeição: média = {}     std = {}'.format(media_r,dp_r))
print('Sem rejeição: média = {}     std = {}'.format(media_s,dp_s))

# Histogramas

plt.rcParams.update({
    'font.family': 'serif',
	'mathtext.fontset': 'cm'
})

num_bins = 30
ymax = 300

fig, axes = plt.subplots(nrows=2,ncols=1)
fig.set_size_inches(7.5,7)

ax = axes[0] 
nr, bins_r, pr = ax.hist(pir,bins=num_bins,color='seagreen') # com rejeição
ax.vlines(x=media_r, ymin=0, ymax=np.max(nr),color='darkred',label='Média')
# Para adicionar um tick em pi:
locs, labels = ax.get_xticks(), ax.get_xticklabels()
locsy = ax.get_yticks()
newlocs = np.append(locs,pi)
newlabels = np.around(np.copy(locs),3)
newlabels = np.append(newlabels,'$\pi$') # Se simplesmente adicionar a label em latex, as outras labels vão sumir
ax.set_xlim(locs[0],locs[-1])
ax.text(locs[1], locsy[3], '$\\bar x = {:.4f} \\pm {:.4f}$'.format(media_r,dp_r), color='darkred', fontsize=12)
ax.legend()
ax.set_title('Com rejeição')

ax = axes[1]
ns, bins_s, ps = ax.hist(pis,bins=num_bins,color='darkcyan') # sem rejeição
ax.vlines(x=media_s, ymin=0, ymax=np.max(ns),color='darkred',label='Média')
ax.vlines(x=pi, ymin=0, ymax=np.max(ns),color='black',label='Valor de $\\pi$')
# Para adicionar um tick em pi:
locs, labels = ax.get_xticks(), ax.get_xticklabels()
locsy = ax.get_yticks()
newlocs = np.append(locs,pi)
newlabels = np.around(np.copy(locs),3)
newlabels = np.append(newlabels,'$\pi$') # Se simplesmente adicionar a label em latex, as outras labels vão sumir
ax.set_xticks(newlocs,labels=newlabels)
ax.set_xlim(locs[0],locs[-1])
ax.text(locs[1], locsy[2], '$\\bar x = {:.4f} \\pm {:.4f}$'.format(media_s,dp_s), color='darkred', fontsize=12)
ax.legend()
ax.set_title('Sem rejeição')

fig.suptitle('Estimativa final de $\pi$ por caminhada markoviana')
fig.supylabel('Frequência')
fig.supxlabel('Valor estimado de $\pi$')
plt.savefig('hist_pi_ex08.png',dpi=1500)
plt.show()
