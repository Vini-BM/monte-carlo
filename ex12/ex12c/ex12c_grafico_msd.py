import numpy as np
import matplotlib.pyplot as plt

mean_file = 'mean_sawwalker.txt'
single_file = 'sawwalker_1692135078.8989353.dat'

# ----- Leitura dos dados -----

# Cabeçalho
with open(mean_file, 'r') as entry:
	num_walkers = entry.readline()
	num_walkers = num_walkers.split()[-1] # número de caminhantes

# Dados
t, msd = np.loadtxt(mean_file,unpack=True,encoding='latin1') # médio
t1, x1, y1, site1, sd1 = np.loadtxt(single_file,unpack=True,encoding='latin1') # individual

# --------- Gráfico ---------

# Atualizar fonte do LaTeX
plt.rcParams.update({
    'font.family': 'serif',
    'mathtext.fontset': 'cm'
})

analitico = t**(1.5) # solução analítica para o msd
plt.plot(t1, sd1, color='slateblue', label=r'${R^2(t)}$')
plt.scatter(t, msd, color='indigo', s=8, label=r'$\overline{R^2(t)}$') # desvio quadrático médio
plt.plot(t[275:-1], analitico[275:-1], label=r'$t^{3/2}$', color='darkblue') # analítico
plt.xlabel('$t$')
plt.ylabel(r'$\overline{R^2(t)}$')
plt.title(f'Desvio quadrático médio de {num_walkers} caminhantes tipo SAW')
plt.xscale('log')
plt.yscale('log')
plt.legend()
plt.savefig(f'saw_msd_{num_walkers}walkers.png', dpi=1200)
plt.show()
