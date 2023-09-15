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
files_L50 = glob('files/mean_temporal_corr_L50*.txt')
files_L100 = glob('files/mean_temporal_corr_L100*.txt')
filelist = [files_L50, files_L100]
L_list = [50, 100]

# ----- Gráfico -----
fig, axes = plt.subplots(1,2)
fig.set_size_inches(12,6)

for i in range(2):
    ax = axes[i]
    L = L_list[i]
    for data in filelist[i]:
        T = data.split('T')[1].split('.txt')[0]
        mcs, ct = np.loadtxt(data, unpack=True)
        ax.plot(mcs[1:], ct[1:], label=f'T={T}')
    ax.legend()
    ax.set_title(fr'$C(t)$ para L={L}')

fig.suptitle(r'Correlação temporal do Modelo de Ising')
fig.supxlabel(r'$t$ (MCS)')
fig.supylabel(r'$C(t)$')
plt.savefig('grafico_ex16a.png', dpi=1000)
plt.show()
