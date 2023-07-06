import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def gaussiana(x,med,dp):
    expoente = -0.5*((x-media)/dp)**2
    return (1/dp*(np.sqrt(2*np.pi)))*expoente

#file_rej = 'ex08_media_pi_rej.txt'
file_sem = 'ex08_media_pi_sem.txt'

#amostra_r, seed_r, pi_r = np.loadtxt(file_rej,unpack=True,encoding='latin1')
amostra_s, seed_s, pi_s = np.loadtxt(file_sem,unpack=True,encoding='latin1')

#pi_r *= 4
pi_s *= 4

bins = 0.001
pi_s_hist = pi_s/bins
pi_s_hist = pi_s_hist.astype('int')
#plt.plot(pi_s_hist)
#print(pi_s_hist)

pi_value, pi_count = np.unique(pi_s_hist, return_counts=True)
pi_value = pi_value.astype('float') * bins
num_bins = len(pi_value)
print(pi_value)
print(pi_count)

#x_array = np.arange(3.05,3.25,0.0001)
#popt, pcov = curve_fit(gaussiana,pi_s,pi_s_hist)


#plt.hist(pi_r,density=True)
#plt.show()
plt.plot(pi_value,pi_count,color='black')
#plt.xlim(3.13,3.15)
plt.hist(pi_s,bins=num_bins,color='darkblue')
plt.show()
