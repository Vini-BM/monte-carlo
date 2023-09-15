import matplotlib.pyplot as plt
import numpy as np
from glob import glob

# ----- Fonte do LaTeX -----
plt.rcParams.update({
    'font.family': 'serif',
    'mathtext.fontset': 'cm'
})
# ----- Estilo -----
plt.style.use('seaborn-dark-palette')

# ----- Arquivos -----
files = glob('files/mean_chi_mag*.txt')
files.sort(key=len)

# ----- Gráfico -----
fig, axes = plt.subplots(1,2)
fig.set_size_inches(12,6)

for data in files:
    T, chi, mag = np.loadtxt(data, unpack=True)
    L = int(data.split('L')[1].split('.')[0])
    axes[0].plot(T, chi, label=f'L={L}')
    axes[1].plot(T, mag, label=f'L={L}')
axes[0].set_ylabel(r'$\chi(T)$')
axes[0].set_ylim(0)
axes[1].set_ylabel(r'$m(T)$')
axes[1].set_ylim(-0.1)

for i in range(2):
    axes[i].set_xlim(2,3)
    ticks = axes[i].get_xticks()
    yticks = axes[i].get_yticks()
    ticks = np.append(ticks, 2.27)
    labels = [str(round(tick, 2)) for tick in ticks]
    labels[-1] = r'$T_C$'
    axes[i].vlines(2.27, min(yticks), max(yticks), color='grey', ls='--')
    axes[i].set_xticks(ticks)
    axes[i].set_xticklabels(labels)
    axes[i].legend()
fig.supxlabel(r'$T$')
fig.suptitle('Susceptibilidade e magnetização do modelo de Ising')
plt.savefig('grafico_ex17.png', dpi=1000)
plt.show()