import math
from sympy import *
from scipy.optimize import brentq

from TP1.MetodosBusquedaRaices.Biseccion import biseccion
from TP1.MetodosBusquedaRaices.EstimacionConvergencia import estimar_orden_convergencia
from TP1.MetodosBusquedaRaices.NewtonRaphson import newton_raphson
from TP1.MetodosBusquedaRaices.NewtonRaphsonModificado import newton_raphson_mod
from TP1.MetodosBusquedaRaices.PuntoFijo import punto_fijo
from TP1.MetodosBusquedaRaices.RepresentacionHistorias import tabular_historia, graficar_historias
from TP1.MetodosBusquedaRaices.Secante import secante

RADIO = 4.25


def f1(x):
    return 4.25 * math.pi * x ** 2 - (math.pi * x ** 3) / 3 - 180.52


def f1_prima(x):
    return 2 * math.pi * RADIO * x - math.pi * x ** 2


def test_raices():
    graf = {}

    print("Hallando raices de f1 por metodo de Bisección con tolerancia 1e-5")
    raiz, historia_bis_5 = biseccion(f1, (RADIO, 2 * RADIO), 1e-5)
    tabular_historia(historia_bis_5, "biseccion")
    graf["BIS5"] = historia_bis_5

    print("Hallando raices de f1 por metodo de Bisección con tolerancia 1e-13")
    raiz, historia_bis_13 = biseccion(f1, (RADIO, 2 * RADIO), 1e-13)
    tabular_historia(historia_bis_13, "biseccion")
    graf["BIS13"] = historia_bis_13
    print(estimar_orden_convergencia(historia_bis_13))

    print("Hallando raices de f1 por metodo de NR con tolerancia 1e-5")
    raiz, historia_nr_5 = newton_raphson(f1, (RADIO, 2 * RADIO), 1e-5)
    tabular_historia(historia_nr_5, "Newton-Raphson")
    print(estimar_orden_convergencia(historia_nr_5))

    print("Hallando raices de f1 por metodo de NR con tolerancia 1e-13")
    raiz, historia_nr_13 = newton_raphson(f1, (RADIO, 2 * RADIO), 1e-13)
    tabular_historia(historia_nr_13, "Newton-Raphson")

    print("Hallando raices de f1 por metodo de NR modificado con tolerancia 1e-5")
    raiz, historia_nrm_5 = newton_raphson_mod(f1, (RADIO, 2 * RADIO), 1e-5)
    tabular_historia(historia_nrm_5, "Newton-Raphson-MOD")

    print("Hallando raices de f1 por metodo de NR modificado con tolerancia 1e-13")
    raiz, historia_nrm_13 = newton_raphson_mod(f1, (RADIO, 2 * RADIO), 1e-13)
    tabular_historia(historia_nrm_13, "Newton-Raphson-MOD")
    print(estimar_orden_convergencia(historia_nrm_13))


    print("Hallando raices de f1 por metodo de secante con tolerancia 1e-5")
    raiz, historia_sec_5 = secante(f1, (RADIO, 2 * RADIO), 1e-5)
    tabular_historia(historia_sec_5, "Secante")

    print("Hallando raices de f1 por metodo de secante con tolerancia 1e-13")
    raiz, historia_sec_13 = secante(f1, (RADIO, 2 * RADIO), 1e-13)
    tabular_historia(historia_sec_13, "Secante")
    print(estimar_orden_convergencia(historia_sec_13))


    print("Hallando raices de f1 por metodo de punto fijo con tolerancia 1e-5")
    raiz, historia_pf_5 = punto_fijo("4.25 * pi * x ** 2 - (pi * x ** 3) / 3 - 180.52", (RADIO, 6), 1e-5, 200)
    tabular_historia(historia_pf_5, "Punto Fijo")

    print("Hallando raices de f1 por metodo de punto fijo con tolerancia 1e-13")
    raiz, historia_pf_13 = punto_fijo("4.25 * pi * x ** 2 - (pi * x ** 3) / 3 - 180.52", (RADIO, 6), 1e-13, 200)
    print(estimar_orden_convergencia(historia_pf_13))

    # print("Hallando raices de f1 por metodo brentq incluido en scipy.optimize")
    # print(brentq(f1, 0, 2 * RADIO))

def test_raices_derivada():
    graf = {}

#    print("Hallando raices de f1 por metodo de Bisección con tolerancia 1e-5")
#    raiz, historia_bis_5 = biseccion(f1_prima, (RADIO, 2 * RADIO), 1e-5)
#    tabular_historia(historia_bis_5, "biseccion")
#    graf["BIS5"] = historia_bis_5
#
#    print("Hallando raices de f1 por metodo de Bisección con tolerancia 1e-13")
#    raiz, historia_bis_13 = biseccion(f1_prima, (RADIO, 2 * RADIO), 1e-13)
#    tabular_historia(historia_bis_13, "biseccion")
#    graf["BIS13"] = historia_bis_13
#    # graficar_historias(graf)

    print("Hallando raices de f1 por metodo de NR con tolerancia 1e-5")
    raiz, historia_nr_5 = newton_raphson(f1_prima, (RADIO, 2 * RADIO), 1e-5)
    tabular_historia(historia_nr_5, "Newton-Raphson")

    print("Hallando raices de f1 por metodo de NR con tolerancia 1e-13")
    raiz, historia_nr_13 = newton_raphson(f1_prima, (RADIO, 2 * RADIO), 1e-13)
    tabular_historia(historia_nr_13, "Newton-Raphson")

    print("Hallando raices de f1 por metodo de NR modificado con tolerancia 1e-5")
    raiz, historia_nrm_5 = newton_raphson_mod(f1_prima, (RADIO, 2 * RADIO), 1e-5)
    tabular_historia(historia_nrm_5, "Newton-Raphson-MOD")

    print("Hallando raices de f1 por metodo de NR modificado con tolerancia 1e-13")
    raiz, historia_nrm_13 = newton_raphson_mod(f1_prima, (RADIO, 2 * RADIO), 1e-13)
    tabular_historia(historia_nrm_13, "Newton-Raphson-MOD")

    print("Hallando raices de f1 por metodo de secante con tolerancia 1e-5")
    raiz, historia_sec_5 = secante(f1_prima, (RADIO, 2 * RADIO), 1e-5)
    tabular_historia(historia_sec_5, "Secante")

    print("Hallando raices de f1 por metodo de secante con tolerancia 1e-13")
    raiz, historia_sec_13 = secante(f1_prima, (RADIO, 2 * RADIO), 1e-13)
    tabular_historia(historia_sec_13, "Secante")

    print("Hallando raices de f1 por metodo de punto fijo con tolerancia 1e-5")
    raiz, historia_pf_5 = punto_fijo("2 * math.pi * RADIO * x - math.pi * x ** 2", (RADIO, 6), 1e-5, 200)
    tabular_historia(historia_pf_5, "Punto Fijo")

    print("Hallando raices de f1 por metodo de punto fijo con tolerancia 1e-13")
    raiz, historia_pf_13 = punto_fijo("2 * math.pi * RADIO * x - math.pi * x ** 2", (RADIO, 6), 1e-13, 200)
    tabular_historia(historia_pf_13, "Punto Fijo")

if __name__ == "__main__":
    test_raices()
