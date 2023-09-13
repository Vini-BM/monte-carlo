import matplotlib.pyplot as plt
import numpy as np
from glob import glob

files_t = glob('files/temporal_corr*T2.27.dat')

for data in files_t:
    L = int(data.split('L')[1].split('_')[0])
    mcs, ct = np.loadtxt(data, unpack=True)
    plt.plot(mcs, ct, label=f'L={L}')
plt.xlabel(r'$t$ (MCS)')
plt.ylabel(r'$C(t)$')
plt.legend()
plt.show()
