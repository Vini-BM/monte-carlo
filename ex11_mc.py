import matplotlib.pyplot as plt
import numpy as np
import random as rd

N = int(1e5)

# Exemplo 5
px = []
for i in range(N):
    r = rd.random()
    x = -1*np.log(1-r)
    px.append(x)
x_array = np.arange(0,10,0.1)
px_an = np.exp(-1*x_array)
plt.hist(px,bins=1000,density=True,color='purple')
plt.plot(x_array,px_an,color='black')
plt.xlim(0,3)
plt.xlabel('$x$')
plt.ylabel('$p(x)$')
plt.yscale('log')
plt.savefig('grafico_ex11_5.png', dpi=1500)
plt.show()

# Exemplo 6

