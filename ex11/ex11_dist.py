import matplotlib.pyplot as plt
import numpy as np
import random as rd

# Fonte para os gráficos
plt.rcParams.update({
    'font.family': 'serif',
	'mathtext.fontset': 'cm'
})

# Exemplo 5
N = int(1e5)
px5 = []
for i in range(N):
    r = rd.random()
    x = -1*np.log(1-r)
    px5.append(x)
x5_array = np.arange(0,10,0.1)
px5_an = np.exp(-1*x5_array)
plt.hist(px5,bins=1000,density=True,color='purple',label='Simulação')
plt.plot(x5_array,px5_an,color='black',label='Analítico')
plt.xlim(0,3)
plt.xlabel('$x$')
plt.ylabel('$p(x)$')
plt.title('Distribuição de probabilidade $p(x) = \\exp (-x)$')
plt.legend()
plt.yscale('log')
plt.savefig('grafico_ex11_5.png', dpi=1500)
plt.show()

# Exemplo 6
N = int(1e6)
px6 = []
tau = 0.4
for j in range(N):
    r = rd.random()
    x = r**(1/(1-tau))
    px6.append(x)
x6_array = np.arange(0.0001,1,0.0001)
px6_an = (1-tau)*x6_array**(-1*tau)
plt.hist(px6,bins=1000,density=True,log=True,color='purple',label='Simulação')
plt.plot(x6_array,px6_an,color='black',label='Analítico')
plt.xlim(0.01,1)
plt.ylim(ymax=10)
plt.xlabel('$x$')
plt.ylabel('$p(x)$')
plt.title('Distribuição de probabilidade $p(x) = (1 - \\tau)x^\\tau$ para $\\tau = {}$'.format(tau))
plt.legend()
plt.xscale('log')
plt.yscale('log')
plt.savefig('grafico_ex11_6.png', dpi=1500)
plt.show()
