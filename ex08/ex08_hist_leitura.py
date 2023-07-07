import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from math import pi

def gaussiana(x,media,dp):
    expoente = -0.5*((x-media)/dp)**2
    return (1/dp*(np.sqrt(2*np.pi)))*np.exp(expoente)

file_rej = 'media_pi_rej_105.txt'
file_sem = 'media_pi_sem_105.txt'

amostra_r, seed_r, pir = np.loadtxt(file_rej,unpack=True,encoding='latin1')
amostra_s, seed_s, pis = np.loadtxt(file_sem,unpack=True,encoding='latin1')

pir *= 4
pis *= 4

bins = 0.005
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

media_r = np.mean(pir_value)
media_s = np.mean(pis_value)
dp_r = np.sqrt(np.var(pir_value))
dp_s = np.sqrt(np.var(pis_value))
xr = np.linspace(pir_value[0],pir_value[-1],num=100)
xs = np.linspace(pis_value[0],pis_value[-1],num=100)
yr = gaussiana(xr,media_r,dp_r)*bins*num_bins_r
ys = gaussiana(xs,media_s,dp_s)*bins*num_bins_s

plt.title('Estimativa final de $\pi$ pelo método com rejeição')
plt.hist(pir,bins=num_bins_r)
plt.vlines(x=pi, ymin=0, ymax=np.max(pir_count),color='black')
# Para adicionar um tick em pi:
locs, labels = plt.xticks()
newlocs = np.append(locs,pi)
newlabels = np.around(np.copy(locs),3)
newlabels = np.append(newlabels,'$\pi$') # Se simplesmente adicionar a label em latex, as outras labels vão sumir
plt.ylabel('Frequência')
plt.xlabel('Valor estimado de $\pi$')
plt.show()

plt.title('Estimativa final de $\pi$ pelo método sem rejeição')
plt.hist(pis,bins=num_bins_s)
plt.vlines(x=pi, ymin=0, ymax=np.max(pis_count),color='black')
# Para adicionar um tick em pi:
locs, labels = plt.xticks()
newlocs = np.append(locs,pi)
newlabels = np.around(np.copy(locs),3)
newlabels = np.append(newlabels,'$\pi$') # Se simplesmente adicionar a label em latex, as outras labels vão sumir
#print(newlocs)
#print(newlabels)

plt.xticks(ticks=newlocs,labels=newlabels)
plt.ylabel('Frequência')
plt.xlabel('Valor estimado de $\pi$')
plt.show()

