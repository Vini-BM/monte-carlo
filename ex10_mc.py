import matplotlib.pyplot as plt
import random as r

def integrando(x,gamma):
    return x**gamma

def amostragem_direta(N,funcao,intervalo=[0,1],gamma=0.8,seed=''):
    r.seed(seed)
    gp, gn = gamma, -1*gamma
    gp_list, gn_list, n_list = [], [], []
    i_gp, i_gn = 0, 0
    for i in range(1,int(N+1)):
        x = r.random()
        i_gp += funcao(x,gp)*abs(intervalo[1]-intervalo[0])/i
        i_gn += funcao(x,gn)*abs(intervalo[1]-intervalo[0])/i
        gp_list.append(i_gp)
        gn_list.append(i_gn)
        n_list.append(i)
    return n_list, gp_list, gn_list

N = 1e5
n, int_p, int_n = amostragem_direta(N,integrando)
plt.plot(n,int_p)
plt.show()
plt.plot(n,int_n)
plt.show()
