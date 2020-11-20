from matplotlib import pyplot as plt
import numpy


def estimar_orden_convergencia(historia):

    alfa = []

    for n in range(2, len(historia) - 1):
        e_n_mas_1 = historia[n+1] - historia[n]
        e_n = historia[n] - historia[n-1]
        e_n_menos_1 = historia[n-1] - historia[n-2]

        alfa.append(numpy.log10(numpy.abs(e_n_mas_1/e_n)) / numpy.log10(numpy.abs(e_n/e_n_menos_1)))

    print(alfa)

    return alfa

#def estimar_constante_convergencia(historia):
