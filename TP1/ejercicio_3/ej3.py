import math
import sys
from sympy import *
from matplotlib import pyplot as plt
from scipy.optimize import brentq

from TP1.MetodosBusquedaRaices.Biseccion import biseccion
from TP1.MetodosBusquedaRaices.EstimacionConvergencia import estimar_orden_convergencia
from TP1.MetodosBusquedaRaices.NewtonRaphson import newton_raphson
from TP1.MetodosBusquedaRaices.NewtonRaphsonModificado import newton_raphson_mod
from TP1.MetodosBusquedaRaices.PuntoFijo import punto_fijo
from TP1.MetodosBusquedaRaices.RepresentacionHistorias import graficar, tabular_historia_precision5, \
    tabular_historia_precision13
from TP1.MetodosBusquedaRaices.Secante import secante
from TP1.MetodosBusquedaRaices.CalculadoraRaices import *

RADIO = 4.25


def f1(x):
    return 4.25 * math.pi * x ** 2 - (math.pi * x ** 3) / 3 - 180.52


def f1_prima(x):
    return 2 * math.pi * RADIO * x - math.pi * x ** 2


def test_raices():  # comentamos los graficos de convergencia pues no pudimos debuggear
    graf_historia_5 = {}
    graf_historia_13 = {}
    graf_convergencia_13 = {}

    raiz, historia_bis_5, it = biseccion(f1, (0, 2 * RADIO), 1e-5)
    tabular_historia_precision5(historia_bis_5, "Biseccion 1e-5", it)
    graf_historia_5["BIS5"] = historia_bis_5

    raiz, historia_nr_5, it = newton_raphson(f1, (RADIO, 2 * RADIO), 1e-5)
    tabular_historia_precision5(historia_nr_5, "Newton-Raphson", it)
    graf_historia_5["NR5"] = historia_nr_5
    # print(estimar_orden_convergencia(historia_nr_5, it))

    # graf_convergencia["NR5"] = estimar_orden_convergencia(historia_nr_5)

    raiz, historia_nrm_5, it = newton_raphson_mod(f1, (RADIO, 2 * RADIO), 1e-5)
    tabular_historia_precision5(historia_nrm_5, "Newton-Raphson-MOD", it)
    graf_historia_5["NRM5"] = historia_nrm_5
    # print(estimar_orden_convergencia(historia_nrm_5, it))
    ##graf_convergencia["NRM5"] = estimar_orden_convergencia(historia_nrm_5)

    raiz, historia_sec_5, it = secante(f1, (RADIO, 2 * RADIO), 1e-5)
    tabular_historia_precision5(historia_sec_5, "Secante", it)
    graf_historia_5["SEC5"] = historia_sec_5
    # print(estimar_orden_convergencia(historia_sec_5, it))
    ##graf_convergencia["SEC5"] = estimar_orden_convergencia(historia_sec_5)

    raiz, historia_pf_5, it = punto_fijo("4.25 * pi * x ** 2 - (pi * x ** 3) / 3 - 180.52", (RADIO, 6), 1e-5)
    tabular_historia_precision5(historia_pf_5, "Punto Fijo", it)
    graf_historia_5["PF5"] = historia_pf_5
    ##graf_convergencia["PF5"] = estimar_orden_convergencia(historia_pf_5)

    raiz, historia_bis_13, it = biseccion(f1, (0, 2 * RADIO), 1e-13)
    tabular_historia_precision13(historia_bis_13, "Biseccion 1e-13", it)
    graf_historia_13["BIS13"] = historia_bis_13
    graf_convergencia_13["BIS"] = estimar_orden_convergencia(historia_bis_13, it)
    # graf_convergencia["BIS5"] = estimar_orden_convergencia(historia_bis_5)

    raiz, historia_nr_13, it = newton_raphson(f1, (RADIO, 2 * RADIO), 1e-13)
    tabular_historia_precision13(historia_nr_13, "Newton-Raphson", it)
    graf_historia_13["NR13"] = historia_nr_13
    graf_convergencia_13["NR13"] = estimar_orden_convergencia(historia_nr_13, it)
    # graf_convergencia["NR5"] = estimar_orden_convergencia(historia_nr_5)

    raiz, historia_nrm_13, it = newton_raphson_mod(f1, (RADIO, 2 * RADIO), 1e-13)
    tabular_historia_precision13(historia_nrm_13, "Newton-Raphson-MOD", it)
    graf_historia_13["NRM13"] = historia_nrm_13
    graf_convergencia_13["NRM13"] = estimar_orden_convergencia(historia_nrm_13, it)
    ##graf_convergencia["NRM5"] = estimar_orden_convergencia(historia_nrm_5)

    raiz, historia_sec_13, it = secante(f1, (RADIO, 2 * RADIO), 1e-13)
    tabular_historia_precision13(historia_sec_13, "Secante", it)
    graf_historia_13["SEC13"] = historia_sec_13
    graf_convergencia_13["SEC13"] = estimar_orden_convergencia(historia_sec_13, it)
    # print(estimar_orden_convergencia(historia_sec_13, it))
    ##graf_convergencia["SEC5"] = estimar_orden_convergencia(historia_sec_5)

    raiz, historia_pf_13, it = punto_fijo("4.25 * pi * x ** 2 - (pi * x ** 3) / 3 - 180.52", (RADIO, 6), 1e-13)
    tabular_historia_precision13(historia_pf_13, "Punto Fijo", it)
    graf_historia_13["PF13"] = historia_pf_13
    graf_convergencia_13["PF13"] = estimar_orden_convergencia(historia_pf_13, it)
    ##graf_convergencia["PF5"] = estimar_orden_convergencia(historia_pf_5)

    # graficar(graf_convergencia)

    graficar(graf_historia_5)
    graficar(graf_historia_5)
    graficar(graf_historia_13)
    graficar(graf_historia_13)

    graficar(graf_convergencia_13)
    graficar(graf_convergencia_13)
    print("Hallando raices de f1 por metodo brentq incluido en scipy.optimize")
    print(brentq(f1, 0, 2 * RADIO))


def raices_derivada():
    print("La raices de la derivada calculada con la calculadora del punto 2" + str(
        calcular_raices(math.pi, 2 * math.pi * RADIO, 0, 1e-7)))


if __name__ == "__main__":
    test_raices()
    raices_derivada()
