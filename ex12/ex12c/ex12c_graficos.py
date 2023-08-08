import numpy as np
import matplotlib.pyplot as plt
from glob import glob

# --------- Leitura dos dados ---------
cam_list = glob('sawwalker*.txt') # lista de arquivos dos caminhantes
num_walkers = int(len(cam_list))
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

# --------- Calculando o desvio quadrático médio dos caminhantes ---------

# Como a simulação de cada amostra tem um número de passos variável,
# é preciso fazer a média sobre os intervalos comuns a todas as amostras.
# A ideia é separar o maior intervalo, da amostra mais velha,
# em intervalos menores comuns a outras amostras, e calcular
# a média pela média desses intervalos menores, com número de amostras diferente.

longest_t = max(tlist, key=len) # tempo da amostra mais 'velha'
longest_sd = max(sdlist, key=len) # desvio quadrático da amostra mais 'velha'

maxlen = len(longest_t) # comprimento da amostra mais velha
reshaped_sdlist = [] # lista para os novos arrays
for sd in sdlist: # loop sobre os arrays do sd
    sdlen = len(sd) # comprimento do sd em questão
    fill = maxlen - sdlen # número de elementos que falta para o array ter o comprimento da amostra mais velha
    fill_array = np.full(fill,np.nan) # array preenchido com NaN de comprimento igual a diferença anterior
    reshaped_sd = np.append(sd,fill_array) # novo array para o sd é o array antigo com o número correto de NaN adicionado ao final
    reshaped_sdlist.append(reshaped_sd) # adicionar novo array na lista

msd = np.nanmean(reshaped_sdlist, axis=0) # a função np.nanmean realiza a média sobre os elementos numéricos, desconsiderando os NaN
# Realiza o procedimento descrito acima, mas de forma sucinta
# Repare que não é a mesma coisa que adicionar zeros nos arrays, porque a média ficaria errada 

# --------- Gráficos ---------

# Atualizar fonte do LaTeX
plt.rcParams.update({
    'font.family': 'serif',
    'mathtext.fontset': 'cm'
})

# Todos os caminhantes:

tarray = np.arange(0, len(msd), 1)
analitico = tarray**(3/2)
plt.scatter(tarray, msd, color='darkred') # desvio quadrático médio
plt.plot(analitico, label=r't^{3/2}', color='darkblue')
plt.xlabel('$t$')
plt.ylabel(r'$\overline{R^2(t)}$')
plt.title('Desvio quadrático médio dos caminhantes tipo SAW')
plt.xscale('log')
plt.yscale('log')
plt.show()
#plt.savefig(f'saw_msd_{num_walkers}walkers.png', dpi=1200)