import numpy as np
import matplotlib.pyplot as plt
from glob import glob

# ---- Arquivos -----
files = glob('files/uniformising*.dat')
files.sort(key=len)


# ----- Fonte do LaTeX -----
plt.rcParams.update({
    'font.family': 'serif',
    'mathtext.fontset': 'cm'
})

# ----- Leitura dos dados -----
energy_list, mag_list, L_list = [], [], []
for datafile in files:
    # Valor de L
    L = int(datafile.split('L')[1].split('.')[0])
    L_list.append(L)
    # Leitura dos dados
    energy, mag = np.loadtxt(datafile, unpack=True, usecols=(0,1))
    energy_list.append(energy)
    mag_list.append(mag)

#  ----- Histograma -----
fig, axes = plt.subplots(1,2) # dois sublplots
fig.set_size_inches(12,6)

for energy, mag, L in zip(energy_list, mag_list, L_list):
    ax = axes[0] # energia
    ax.hist(energy, density=True, bins=25, alpha=0.7, label=f'$L={L}$')
    ax.set_xlabel(r'$E/N$')
    ax.set_xlim(-0.9, 0.9)
    ax.legend()
    ax = axes[1] # magnetização
    ax.hist(mag, density=True, bins=25, alpha=0.7, label=f'$L={L}$')
    ax.set_xlabel(r'$m$')
    ax.legend()

fig.supylabel('Densidade de probabilidade')
fig.suptitle(fr'Energia e magnetização do modelo de Ising')
plt.savefig('grafico_ex14.png', dpi=1000)
plt.show()
