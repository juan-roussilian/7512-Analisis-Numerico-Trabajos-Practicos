import numpy as np


def estimar_orden_convergencia(historia, it):


   alfa = np.zeros((it - 3, 2))
   for n in range(2, it - 1):
        e_n_mas_1 = historia[n+1][1] - historia[n][1]
        e_n = historia[n][1] - historia[n-1][1]
        e_n_menos_1 = historia[n-1][1] - historia[n-2][1]

        division_1 = e_n_mas_1/e_n
        division_2 = e_n/e_n_menos_1
        alfa[n-2] = n, np.log10(np.abs(division_1))/ np.log10(np.abs(division_2))

   return alfa

def estimar_constante_asintontica(historia, alfa):
    constante =  np.zeros( (historia.size, 2))
    aux = [x[1] for x in historia]

    for n in range(1, len(aux) - 2):
        e_n_mas_1 = historia[n+1][1] - historia[n][1]
        e_n = historia[n][1] - historia[n-1][1]
        constante[n] = (abs(e_n_mas_1)/abs((e_n)) ** alfa)

    return constante