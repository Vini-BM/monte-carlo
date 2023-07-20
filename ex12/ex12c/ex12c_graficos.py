import numpy as np
import matplotlib.pyplot as plt
from glob import glob

# --------- Leitura dos dados ---------
cam_list = glob('sawwalker*.txt') # lista de arquivos dos caminhantes
tlist, xlist, ylist, sitelist = [], [], [], []
sdlist = []
for file in cam_list:
    t, x, y, site = np.loadtxt(file,unpack=True,encoding='latin1')
    sd = x**2 + y**2
    tlist.append(t)
    xlist.append(x)
    ylist.append(y)
    sitelist.append(site)
    sdlist.append(sd)

longest_t = max(tlist, key=len)
longest_sd = max(sdlist, key=len)

# --------- Gráficos ---------

# Atualizar fonte do LaTeX
plt.rcParams.update({
    'font.family': 'serif',
    'mathtext.fontset': 'cm'
})

# Todos os caminhantes:
msd = np.mean(longest_sd, axis=0)
plt.plot(msd)
plt.show()
