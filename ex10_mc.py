import matplotlib.pyplot as plt
import random as rand
import numpy as np

# Funções

def integrando(x,gamma):
    return x**gamma

def amostragem_direta(N,funcao,gamma,zeta,seed=''):
    rand.seed(seed)
    gp, gn = gamma, -1*gamma
    gp_list, gn_list, n_list = [], [], []
    gp_analitico, gn_analitico = 1/(1+gp), 1/(1+gn)
    i_gp, i_gn = 0, 0
    const = 1/(1+zeta)
    for j in range(1,int(N+1)):
        r = rand.random()
        x = r**const
        i_gp += funcao(x,gp-zeta)
        print(i_gp)
        i_gn += funcao(x,gn-zeta)
        print(i_gn)
        gp_list.append(i_gp/j)
        gn_list.append(i_gn/j)
        n_list.append(j)
    gp_list = np.asarray(gp_list)*const
    gn_list = np.asarray(gn_list)*const
    return n_list, gp_list, gn_list, gp_analitico, gn_analitico

# Simulação
N = 1e5
gamma = 0.2
zeta = -0.2
n, int_p, int_n, p_analitico, n_analitico = amostragem_direta(N,integrando,gamma,zeta)

#print(int_p)
#print(int_n)

# Gráfico para gamma positivo
plt.plot(n, int_p, label='Integral numérica', color='darkred', lw=1)
plt.hlines(p_analitico, xmin=0, xmax=N, label='Integral analítica', color='darkgreen', lw=1.5)
#plt.xlim(0,100)
#plt.ylim(0.5,0.6)
plt.title('Convergência da integral por amostragem direta')
plt.xlabel('$N$')
plt.ylabel('$I({})$'.format(gamma))
plt.legend()
plt.show()

# Gráfico para gamma negativo
plt.plot(n, int_n, label='Integral numérica', color='darkred', lw=1)
#plt.hlines(n_analitico, xmin=0, xmax=N, label='Integral analítica', color='darkgreen', lw=1.5)
#plt.xlim(0,100)
#plt.ylim(4.2,5.2)
plt.title('Convergência da integral por amostragem direta')
plt.xlabel('$N$')
plt.ylabel('$I({})$'.format(-1*gamma))
plt.legend()
plt.show()
