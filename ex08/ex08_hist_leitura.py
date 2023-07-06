import numpy as np
import matplotlib.pyplot as plt

file_rej = 'ex08_media_pi_rej.txt'
file_sem = 'ex08_media_pi_sem.txt'

amostra_r, seed_r, pi_r = np.loadtxt(file_rej,unpack=True,encoding='latin1')
amostra_s, seed_s, pi_s = np.loadtxt(file_sem,unpack=True,encoding='latin1')

pi_r *= 4
pi_s *= 4

pi_r = np.sort(pi_r)
pi_s = np.sort(pi_s)

print(pi_r)
print(pi_s)

plt.hist(pi_r,density=True)
plt.show()
plt.hist(pi_s,density=True)
plt.show()
