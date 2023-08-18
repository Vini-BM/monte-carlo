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

#  ----- Gráfico -----
for datafile in files:

    # Valor de L
    L = int(datafile.split('L')[1].split('.')[0])
    
    # Leitura dos dados
    energy, mag = np.loadtxt(datafile, unpack=True, usecols=(0,1))
    
    # Histograma
    fig, axes = plt.subplots(1,2)
    ax = axes[0] # energia
    ax.hist(energy, density=True, color='darkgreen')
    ax.set_ylabel(r'$E/N$')
    ax = axes[1] # magnetização
    ax.hist(mag, density=True, color='darkorange')
    ax.set_ylabel(r'$m$')
    fig.supxlabel('Contagem')
    fig.suptitle(fr'Energia e magnetização do modelo de Ising para $L={L}$')
    plt.show()
