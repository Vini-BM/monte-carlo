import numpy as np
import matplotlib.pyplot as plt
from glob import glob

# ----- Fonte do LaTeX -----
plt.rcParams.update({
    'font.family': 'serif',
    'mathtext.fontset': 'cm'
})

filelist_hom = glob('files/metropolis*T1_hom.dat')
filelist_rand = glob('files/metropolis*T1_rand.dat')

for hom, rand in zip(filelist_hom, filelist_rand):
    # ----- Leitura dos dados -----
    mcs_h, en_h, mag_h = np.loadtxt(hom,unpack=True)
    mcs_rand, en_rand, mag_rand = np.loadtxt(rand,unpack=True)
    L = int(hom.split('L')[1].split('_')[0])
    # ----- Gráficos -----
    fig, axes = plt.subplots(1,2)
    fig.set_size_inches(16,6)
    ax = axes[0] # esquerda: energia
    ax.plot(mcs_h, en_h, label=r'$m(0)=1$', color='darkblue')
    ax.plot(mcs_rand, en_rand, label='Estado inicial aleatório', color='darkred')
    ax.set_xlim(0,300)
    ax.set_ylabel(r'$E(t)/N$')
    ax.legend()
    ax = axes[1] # direita: magnetização
    ax.plot(mcs_h, np.abs(mag_h), label=r'$m(0)=1$', color='darkblue')
    ax.plot(mcs_rand, np.abs(mag_rand), label='Estado inicial aleatório', color='darkred')
    ax.set_xlim(0,300)
    ax.set_ylabel(r'$|m(t)|$')
    ax.legend()
    fig.suptitle(f'Energia e magnetização do modelo de Ising com T=1 e L={L}')
    fig.supxlabel(r'$t$ (MCS)')
    plt.savefig(f'grafico_ex15_L{L}_T1.png', dpi=1000)
    plt.show()