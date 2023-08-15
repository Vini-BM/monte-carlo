import numpy as np
import matplotlib.pyplot as plt

mean_file = 'mean_walker.txt'
single_file = 'walker_1692128640.9239476.dat'

# ----- Leitura dos dados -----

# Cabeçalho
with open(mean_file, 'r') as entry:
	num_walkers = entry.readline()
	num_walkers = num_walkers.split()[-1] # número de caminhantes

# Dados
t, msd = np.loadtxt(mean_file,unpack=True,encoding='latin1') # médio
t1, x1, y1, sd1 = np.loadtxt(single_file,unpack=True,encoding='latin1') # individual

# ----- Gráfico -----

# Atualizar fonte do LaTeX
plt.rcParams.update({
    'font.family': 'serif',
    'mathtext.fontset': 'cm'
})

plt.plot(sd1,color='lightcoral',label=r'$R^2(t)$')
plt.plot(msd,color='darkred',label=r'$\overline{{R^2(t)}}$')
plt.plot(t,color='darkblue',ls='--',label=r'$t$')
plt.legend()
plt.xlabel(r'$t$')
plt.ylabel(r'$\overline{{R^2(t)}}$')
plt.title(f'Deslocamento quadrático de {num_walkers} caminhantes')
plt.savefig(f'msd_{num_walkers}walkers.png', dpi=1200)
plt.show()