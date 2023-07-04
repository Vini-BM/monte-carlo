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
gamma = 0.8
zeta = -0.7
n, int_p, int_n, p_analitico, n_analitico = amostragem_direta(N,integrando,gamma,zeta)

# Simulação da amostragem direta
n_d, int_p_d, int_n_d, p_analitico_d, n_analitico_d = amostragem_direta(N,integrando,gamma,0)


# Gráfico para gamma positivo
plt.plot(n, int_p, label='Amostragem por relevância', color='darkred', lw=1)
plt.plot(n, int_p_d, label='Amostragem direta', color='darkblue', lw=1)
plt.hlines(p_analitico, xmin=0, xmax=N, label='Integral analítica', color='darkgreen', lw=1.5)
plt.xlim(xmin=0)
plt.ylim(0.5,0.6)
plt.title('Convergência da integral')
plt.xlabel('$N$')
plt.ylabel('$I({})$'.format(gamma))
plt.legend()
plt.show()

# Gráfico para gamma negativo
plt.plot(n, int_n, label='Amostragem por relevância', color='darkred', lw=1)
plt.plot(n, int_n_d, label='Amostragem direta', color='darkblue', lw=1)
plt.hlines(n_analitico, xmin=0, xmax=N, label='Integral analítica', color='darkgreen', lw=1.5)
plt.xlim(xmin=0)
plt.ylim(4.2,5.2)
plt.title('Convergência da integral')
plt.xlabel('$N$')
plt.ylabel('$I({})$'.format(-1*gamma))
plt.legend()
plt.savefig('grafico_ex11_7.png',dpi=1500)
plt.show()
