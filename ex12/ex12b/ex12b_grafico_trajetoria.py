import matplotlib.pyplot as plt
import numpy as np
from glob import glob

# --------- Leitura dos dados ---------
cam_list = glob('latticewalker*.dat') # lista de arquivos dos caminhantes
tlist, xlist, ylist, sitelist, sdlist = [], [], [], [], []
for file in cam_list:
    t, x, y, site, sd = np.loadtxt(file,unpack=True)
    xlist.append(x)
    ylist.append(y)
    sitelist.append(site)
    tlist.append(t)
    sdlist.append(sd)
num_walkers = len(cam_list)
# --------- Gráficos ---------

# Atualizar fonte do LaTeX
plt.rcParams.update({
    'font.family': 'serif',
    'mathtext.fontset': 'cm'
})

# Todos os caminhantes:

for x, y in zip(xlist,ylist):
    plt.plot(x,y) # trajetória
plt.title(f'Trajetória de {num_walkers} caminhantes na rede quadrada')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.savefig(f'trajetoria_{num_walkers}latticewalkers.png', dpi=100)
plt.show()