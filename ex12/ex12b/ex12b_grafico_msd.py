import matplotlib.pyplot as plt
import numpy as np

# ----- Leitura dos dados -----
mean_file = 'mean_latticewalker.txt'
single_file = 'latticewalker_1692133491.9928896.dat'

# Cabeçalho
with open(mean_file, 'r') as entry:
	num_walkers = entry.readline()
	num_walkers = num_walkers.split()[-1] # número de caminhantes

# Dados
t, msd = np.loadtxt(mean_file,unpack=True,encoding='latin1') # médio
t1, x1, y1, site1, sd1 = np.loadtxt(single_file,unpack=True,encoding='latin1') # individual

# ----- Gráfico -----

# Atualizar fonte do LaTeX
plt.rcParams.update({
    'font.family': 'serif',
    'mathtext.fontset': 'cm'
})

plt.plot(sd1,color='palegreen',label=r'$R^2(t)$')
plt.plot(msd,color='darkgreen',label=r'$\overline{{R^2(t)}}$')
plt.plot(t,color='darkblue',ls='--',label=r'$t$')
plt.legend()
plt.xlabel(r'$t$')
plt.ylabel(r'$\overline{{R^2(t)}}$')
plt.title(f'Deslocamento quadrático de {num_walkers} caminhantes na rede quadrada')
plt.savefig(f'msd_{num_walkers}latticewalkers.png', dpi=1200)
plt.show()