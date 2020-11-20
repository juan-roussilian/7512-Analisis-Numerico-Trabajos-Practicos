import math

from matplotlib import pyplot as plt
import numpy as np


def estimar_orden_convergencia(historia, it):

   print("A")

   alfa = np.zeros((it - 3, 2))
   for n in range(2, it - 1):
        e_n_mas_1 = historia[n+1][1] - historia[n][1]
        e_n = historia[n][1] - historia[n-1][1]
        e_n_menos_1 = historia[n-1][1] - historia[n-2][1]

        division_1 = e_n_mas_1/e_n
        division_2 = e_n/e_n_menos_1
        alfa[n-2] = n, np.log10(np.abs(division_1))/ np.log10(np.abs(division_2))

   print("B")
   return alfa

#def estimar_constante_convergencia(historia, alfa):
#    constante = []
#
#    for n in range(1, len(historia) - 1):
#        e_n_mas_1 = historia[n+1] - historia[n]
#        e_n = historia[n] - historia[n-1]
#        constante.append(abs(e_n_mas_1)/abs((e_n))**alfa)
