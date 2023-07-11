import numpy as np
import matplotlib.pyplot as plt
from math import pi

# --------- Gaussiana ---------

def gaussiana(x,media,dp):
    expoente = -0.5*((x-media)/dp)**2
    return np.exp(expoente)/(dp*(np.sqrt(2*pi)))

# --------- Leitura dos dados ---------
	
file_rej = 'media_pi_rej_105.txt'
file_sem = 'media_pi_sem_105.txt'

amostra_r, seed_r, pir = np.loadtxt(file_rej,unpack=True,encoding='latin1')
amostra_s, seed_s, pis = np.loadtxt(file_sem,unpack=True,encoding='latin1')

pir *= 4
pis *= 4

# --------- Estatísticas ---------

# Média dos conjuntos
media_r = np.mean(pir)
media_s = np.mean(pis)
# Desvio padrão dos conjuntos - para a gaussiana
dp_r = np.std(pir)
dp_s = np.std(pis)
# Desvio padrão da média
dpm_r = dp_r/np.sqrt(len(pir)-1)
dpm_s = dp_s/np.sqrt(len(pis)-1)
# Arrays para a gaussiana
xr = np.arange(np.min(pir),np.max(pir),step=0.00001)
xs = np.arange(np.min(pis),np.max(pis),step=0.00001)
yr = gaussiana(xr,media_r,dp_r)
ys = gaussiana(xs,media_s,dp_s)

print('Rejeição: média = {}     std = {}'.format(media_r,dpm_r))
print('Sem rejeição: média = {}     std = {}'.format(media_s,dpm_s))

# --------- Histogramas ---------

# Atualizar fonte do LaTeX
plt.rcParams.update({
    'font.family': 'serif',
	'mathtext.fontset': 'cm'
})

# Parâmetros dos histogramas
num_bins = 30
ymax = 300 # no chute
gaus_color, mean_color = 'indigo', 'darkred' # cores para plotar a curva e escrever os dados

# Definindo subplots
fig, axes = plt.subplots(nrows=2,ncols=1)
fig.set_size_inches(8.5,7)

# Com rejeição:
ax = axes[0] 
nr, bins_r, pr = ax.hist(pir,bins=num_bins,color='seagreen',density=True)
ax.vlines(x=media_r, ymin=0, ymax=np.max(nr),color=mean_color,label='Média') # reta indicando a média
ax.plot(xr,yr,color=gaus_color,label='Gaussiana') # gaussiana
locsx, locsy = ax.get_xticks(), ax.get_yticks()
ax.set_xlim(locsx[0],locsx[-1])
# Escrever valores:
ax.text(locsx[1], locsy[3], r'$\bar x = {:.2f}$'.format(media_r), color=gaus_color, fontsize=12) # Média do conjunto
ax.text(locsx[1], locsy[3]-1, r'$\sigma_{{amostra}} = {:.2f}$'.format(dp_r), color=gaus_color, fontsize=12) # Desvio padrão do conjunto
ax.text(locsx[1], locsy[2], '$\\langle x \\rangle = {:.4f} \\pm {:.4f}$'.format(media_r,dpm_r), color=mean_color, fontsize=12) # Média da distribuição
ax.legend()
ax.set_title('Com rejeição')

# Sem rejeição:
ax = axes[1]
ns, bins_s, ps = ax.hist(pis,bins=num_bins,color='darkcyan',density=True)
#ax.vlines(x=pi, ymin=0, ymax=np.max(ns),color='black',label='Valor de $\\pi$') # reta indicando pi
ax.vlines(x=media_s, ymin=0, ymax=np.max(ns),color=mean_color,label='Média') # reta indicando a média
ax.plot(xs,ys,color=gaus_color,label='Gaussiana') # gaussiana
# Para adicionar um tick em pi:
locsx, locsy = ax.get_xticks(), ax.get_yticks()
labels = ax.get_xticklabels()
newlocs = np.append(locsx,pi)
newlabels = np.around(np.copy(locsx),3)
newlabels = np.append(newlabels,'$\pi$') # Se simplesmente adicionar a label em latex, as outras labels vão sumir
ax.set_xticks(newlocs,labels=newlabels)
ax.set_xlim(locsx[0],locsx[-1])
# Escrever valores:
ax.text(locsx[1], locsy[5], r'$\bar x = {:.2f}$'.format(media_s), color=gaus_color, fontsize=12) # Média do conjunto
ax.text(locsx[1], locsy[5]-1, r'$\sigma_{{amostra}} = {:.2f}$'.format(dp_s), color=gaus_color, fontsize=12) # Desvio padrão do conjunto
ax.text(locsx[1], locsy[3], '$\\langle x \\rangle = {:.4f} \\pm {:.4f}$'.format(media_s,dpm_s), color=mean_color, fontsize=12) # Média da distribuição
ax.legend()
ax.set_title('Sem rejeição')

# Título e eixos
fig.suptitle('Estimativa final de $\pi$ por caminhada markoviana')
fig.supylabel('Distribuição de probabilidade')
fig.supxlabel('Valor estimado de $\pi$')
plt.savefig('hist_pi_ex08.png',dpi=1500)
plt.show()
