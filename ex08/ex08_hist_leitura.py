import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from math import pi

def gaussiana(x,media,dp):
    expoente = -0.5*((x-media)/dp)**2
    return np.exp(expoente)/(dp*(np.sqrt(2*pi)))

file_rej = 'media_pi_rej_105.txt'
file_sem = 'media_pi_sem_105.txt'

amostra_r, seed_r, pir = np.loadtxt(file_rej,unpack=True,encoding='latin1')
amostra_s, seed_s, pis = np.loadtxt(file_sem,unpack=True,encoding='latin1')

pir *= 4
pis *= 4

bins = 0.001
pis_hist = pis/bins
pis_hist = pis_hist.astype('int')
pir_hist = pir/bins
pir_hist = pir_hist.astype('int')

pis_value, pis_count = np.unique(pis_hist, return_counts=True)
pis_value = pis_value.astype('float') * bins
num_bins_s = len(pis_value)

pir_value, pir_count = np.unique(pir_hist, return_counts=True)
pir_value = pir_value.astype('float') * bins
num_bins_r = len(pir_value)

# Fit

media_r = np.mean(pir)
media_s = np.mean(pis)
dp_r = np.sqrt(np.var(pir_value)/(len(pir_value)-1))
dp_s = np.sqrt(np.var(pis_value)/(len(pis_value)-1))
xr = np.arange(np.min(pir_value),np.max(pir_value),step=0.00001)
xs = np.arange(np.min(pis_value),np.max(pis_value),step=0.00001)
yr = gaussiana(xr,media_r,dp_r)*bins*num_bins_r
ys = gaussiana(xs,media_s,dp_s)*bins*num_bins_s

print(num_bins_r,num_bins_s)
print(np.shape(pir),np.shape(pir_value))
print('Rejeição: média = {}     std = {}'.format(media_r,dp_r))
print('Sem rejeição: média = {}     std = {}'.format(media_s,dp_s))

# Histogramas
plt.rcParams.update({
    'font.family': 'serif',
	'mathtext.fontset': 'cm'
})

fig, axes = plt.subplots(nrows=2,ncols=1)
fig.set_size_inches(7.5,7)

ax = axes[0] 
ax.hist(pir,bins=num_bins_r,color='seagreen',density=True) # com rejeição
ax.vlines(x=media_r, ymin=0, ymax=200,color='darkred',label='Média')
ax.plot(xr,yr,color='orange')
#ax.vlines(x=pi, ymin=0, ymax=np.max(pir_count),color='black') # valor de pi
# Para adicionar um tick em pi:
locs, labels = ax.get_xticks(), ax.get_xticklabels()
locsy = ax.get_yticks()
newlocs = np.append(locs,pi)
newlabels = np.around(np.copy(locs),3)
newlabels = np.append(newlabels,'$\pi$') # Se simplesmente adicionar a label em latex, as outras labels vão sumir
#ax.set_xticks(newlocs,labels=newlabels)
ax.set_xlim(locs[0],locs[-1])
ax.text(locs[1], locsy[3], '$\\bar x = {:.4f} \\pm {:.4f}$'.format(media_r,dp_r), color='darkred', fontsize=12)
ax.legend()
ax.set_title('Com rejeição')

ax = axes[1]
ax.hist(pis,bins=num_bins_s,color='darkcyan',density=False) # sem rejeição
ax.vlines(x=media_s, ymin=0, ymax=200,color='darkred',label='Média')
ax.vlines(x=pi, ymin=0, ymax=np.max(pis_count),color='black',label='Valor de $\\pi$')
ax.plot(xs,ys,color='orange')
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
#plt.savefig('hist_pi_ex08.png',dpi=1500)
plt.show()

plt.plot(xs,ys)
plt.plot(xr,yr)
plt.show()
