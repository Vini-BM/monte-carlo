import numpy as np
import matplotlib.pyplot as plt
from glob import glob

# ----- Arquivos -----
files = glob('forestfire*mean.txt')
files.sort(key=len) # para o 50 ficar antes do 100

# ----- Fonte do LaTeX -----
plt.rcParams.update({
    'font.family': 'serif',
    'mathtext.fontset': 'cm'
})

# ----- Gráfico -----
plt.figure(figsize=(10,6)) # tamanho da figura
for file in files:
    L = file.split(sep='L')[1].split(sep='_')[0] # valor de L para a legenda
    p, t = np.loadtxt(file, unpack=True, encoding='latin1') # leitura dos dados
    plt.plot(p, t, label=(f'L = {L}'), marker='s')
pc = 0.5927 # limiar de percolação, para indicar no gráfico
ymax = max(plt.yticks()[0]) # limite do plot
plt.ylim(0,ymax)
plt.vlines(x=pc, ymin=0, ymax=ymax, ls='--', color='grey', label=r'Limiar de percolação $p_c$') # linha vertical em pc
plt.legend()
plt.xlabel(r'$p$')
plt.ylabel(r'$T(p,L)$')
plt.title(r'Tempo de percolação em função de $p$ e $L$')
plt.savefig('forestfire.png', dpi=1200)
plt.show()