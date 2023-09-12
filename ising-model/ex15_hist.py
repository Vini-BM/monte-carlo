import numpy as np
import matplotlib.pyplot as plt
from glob import glob

# ----- Fonte do LaTeX -----
plt.rcParams.update({
    'font.family': 'serif',
    'mathtext.fontset': 'cm'
})
plt.style.use('seaborn-dark-palette')
# ---- Arquivos -----

filelist_50 = glob('files/indep_metropolis_L50_T*.dat')
filelist_100 = glob('files/indep_metropolis_L100_T*.dat')

for L, filelist in zip([50,100],[filelist_50,filelist_100]):
	fig, axes = plt.subplots(2,2)
	fig.set_size_inches(14,12)
	for file in filelist:
		T = int(file.split('T')[1].split('.')[0])
		r = 0 if T==1 else 1 # subplots da primeira linha são para T=1
		mcs, en, mag = np.loadtxt(file, unpack=True, skiprows=4) # fim do transiente, medidas a cada 50
		mag = np.abs(mag)
		axes[r][0].hist(en, density=True, alpha=0.6, label=f'T={T}')
		axes[r][1].hist(mag, density=True, alpha=0.6, label=f'T={T}')
	for r in [0,1]:
		axes[r][0].set_xlabel(r'$E/N$')
		axes[r][0].legend()
		axes[r][1].set_xlabel(r'$|m|$')
		axes[r][1].legend()
	axes[1][1].set_xlim(0,1)
	fig.suptitle(f'Distribuição da energia e magnetização em equilíbrio para L={L}')
	plt.savefig(f'hist_ex15_L{L}.png', dpi=1000)
	plt.show()