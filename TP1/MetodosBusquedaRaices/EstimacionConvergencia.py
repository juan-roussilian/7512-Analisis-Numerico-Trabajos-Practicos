import math

from matplotlib import pyplot as plt
import numpy


def estimar_orden_convergencia(historia):

    alfa = []
    contador_iter = 0
    for n in range(2, len(historia) - 1):
        e_n_mas_1 = historia[n+1] - historia[n]
        e_n = historia[n] - historia[n-1]
        e_n_menos_1 = historia[n-1] - historia[n-2]

        division_1 = e_n_mas_1/e_n
        division_2 = e_n/e_n_menos_1
        log_1 =  math.log(numpy.abs(e_n/e_n_menos_1),10)
        log_2 = math.log(numpy.abs(e_n_mas_1 / e_n),10)

        alfa.append(log_1 /log_2)

    contador_iter += 1
    return alfa

#def estimar_constante_convergencia(historia, alfa):
#    constante = []
#
#    for n in range(1, len(historia) - 1):
#        e_n_mas_1 = historia[n+1] - historia[n]
#        e_n = historia[n] - historia[n-1]
#        constante.append(abs(e_n_mas_1)/abs((e_n))**alfa)
