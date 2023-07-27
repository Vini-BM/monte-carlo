import numpy as np
import matplotlib.pyplot as plt
from glob import glob

# --------- Leitura dos dados ---------
cam_list = glob('sawwalker*.txt') # lista de arquivos dos caminhantes
tlist, xlist, ylist, sitelist = [], [], [], [] # lista para os valores no arquivo
sdlist = [] # lista para o desvio quadrático
for file in cam_list:
    t, x, y, site = np.loadtxt(file,unpack=True,encoding='latin1') # tempo, x, y, sitio
    sd = x**2 + y**2 # desvio quadrático
    tlist.append(t)
    xlist.append(x)
    ylist.append(y)
    sitelist.append(site)
    sdlist.append(sd)

longest_t = max(tlist, key=len) # tempo da amostra mais 'velha'
longest_sd = max(sdlist, key=len) # desvio quadrático da amostra mais 'velha'


# --------- Gráficos ---------

# Atualizar fonte do LaTeX
plt.rcParams.update({
    'font.family': 'serif',
    'mathtext.fontset': 'cm'
})

# Todos os caminhantes:
plt.plot(longest_sd, color='darkred') # desvio quadrático da amostra mais 'velha'
plt.xlabel('$t$')
plt.ylabel('$R^2(t)$')
plt.title('Desvio quadrático do caminhante tipo SAW')
plt.show()
