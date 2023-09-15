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
files_L50 = glob('files/indep_spatial_corr_L50*.dat')
files_L100 = glob('files/indep_spatial_corr_L100*.dat')
filelist = [files_L50, files_L100]
L_list = [50, 100]

# ----- Gráfico -----
fig, axes = plt.subplots(1,2)
fig.set_size_inches(12,6)

for i in range(2):
    ax = axes[i]
    L = L_list[i]
    for data in filelist[i]:
        T = data.split('T')[1].split('.dat')[0]
        r, cr = np.loadtxt(data, unpack=True)
        ax.plot(r, cr, label=f'T={T}')
    ax.legend()
    ax.set_xlim(1,L/2-1)
    ax.set_title(fr'$C(r)$ para L={L}')

fig.suptitle(r'Correlação espacial do Modelo de Ising')
fig.supxlabel(r'$r$')
fig.supylabel(r'$C(r)$')
plt.savefig('grafico_ex16b_novo.png', dpi=1000)
plt.show()
