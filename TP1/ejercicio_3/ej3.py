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
from TP1.MetodosBusquedaRaices.RepresentacionHistorias import tabular_historia, graficar
from TP1.MetodosBusquedaRaices.Secante import secante
from TP1.MetodosBusquedaRaices.CalculadoraRaices import *

RADIO = 4.25


def f1(x):
    return 4.25 * math.pi * x ** 2 - (math.pi * x ** 3) / 3 - 180.52


def f1_prima(x):
    return 2 * math.pi * RADIO * x - math.pi * x ** 2


def test_raices(): #comentamos los graficos de convergencia pues no pudimos debuggear
    graf_historia = {}
    graf_convergencia = {}

    raiz, historia_bis_5, it = biseccion(f1, (0, 2 * RADIO), 1e-5)
    tabular_historia(historia_bis_5, "Biseccion 1e-5", it)
    graf_historia["BIS5"] = historia_bis_5
    #graf_convergencia["BIS5"] = estimar_orden_convergencia(historia_bis_5)

    #print("Hallando raices de f1 por metodo de Bisección con tolerancia 1e-13")
    #raiz, historia_bis_13 = biseccion(f1, (RADIO, 2 * RADIO), 1e-13)
    #tabular_historia(historia_bis_13, "biseccion")
    ##graf_historia["BIS13"] = historia_bis_13
    ##graf_convergencia["BIS13"] = estimar_orden_convergencia(historia_bis_13)

    #print("Hallando raices de f1 por metodo de NR con tolerancia 1e-5")
    raiz, historia_nr_5, it = newton_raphson(f1, (RADIO, 2 * RADIO), 1e-5)
    tabular_historia(historia_nr_5, "Newton-Raphson", it)
    graf_historia["NR5"] = historia_nr_5
    #print(estimar_orden_convergencia(historia_nr_5))
    ##graf_convergencia["NR5"] = estimar_orden_convergencia(historia_nr_5)

    #print("Hallando raices de f1 por metodo de NR con tolerancia 1e-13")
    #raiz, historia_nr_13 = newton_raphson(f1, (RADIO, 2 * RADIO), 1e-13)
    #tabular_historia(historia_nr_13, "Newton-Raphson")
    #print(estimar_orden_convergencia(historia_nr_13))
    ##graf_historia["NR13"] = historia_nr_13
    ##graf_convergencia["NR13"] = estimar_orden_convergencia(historia_nr_13)


    #print("Hallando raices de f1 por metodo de NR modificado con tolerancia 1e-5")
    raiz, historia_nrm_5, it = newton_raphson_mod(f1, (RADIO, 2 * RADIO), 1e-5)
    tabular_historia(historia_nrm_5, "Newton-Raphson-MOD", it)
    graf_historia["NRM5"] = historia_nrm_5
    ##graf_convergencia["NRM5"] = estimar_orden_convergencia(historia_nrm_5)

    #print("Hallando raices de f1 por metodo de NR modificado con tolerancia 1e-13")
    #raiz, historia_nrm_13 = newton_raphson_mod(f1, (RADIO, 2 * RADIO), 1e-13)
    #tabular_historia(historia_nrm_13, "Newton-Raphson-MOD")
    ##graf_historia["NRM13"] = historia_nrm_13
    ##graf_convergencia["NRM13"] = estimar_orden_convergencia(historia_nrm_13)

    #print("Hallando raices de f1 por metodo de secante con tolerancia 1e-5")
    raiz, historia_sec_5, it = secante(f1, (RADIO, 2 * RADIO), 1e-5)
    tabular_historia(historia_sec_5, "Secante", it)
    graf_historia["SEC5"] = historia_sec_5
    ##graf_convergencia["SEC5"] = estimar_orden_convergencia(historia_sec_5)

    #print("Hallando raices de f1 por metodo de secante con tolerancia 1e-13")
    #raiz, historia_sec_13 = secante(f1, (RADIO, 2 * RADIO), 1e-13)
    #tabular_historia(historia_sec_13, "Secante")
    ##graf_historia["SEC13"] = historia_sec_13
    ##graf_convergencia["SEC13"] = estimar_orden_convergencia(historia_sec_13)

    #print("Hallando raices de f1 por metodo de punto fijo con tolerancia 1e-5")
    raiz, historia_pf_5, it = punto_fijo("4.25 * pi * x ** 2 - (pi * x ** 3) / 3 - 180.52", (RADIO, 6), 1e-5, 200)
    tabular_historia(historia_pf_5, "Punto Fijo", it)
    graf_historia["PF5"] = historia_pf_5
    ##graf_convergencia["PF5"] = estimar_orden_convergencia(historia_pf_5)

    #print("Hallando raices de f1 por metodo de punto fijo con tolerancia 1e-13")
    #raiz, historia_pf_13 = punto_fijo("4.25 * pi * x ** 2 - (pi * x ** 3) / 3 - 180.52", (RADIO, 6), 1e-13, 200)
    #tabular_historia(historia_pf_13, "Punto Fijo")
    ##graf_historia["PF13"] = historia_pf_13
    ##graf_convergencia["PF13"] = estimar_orden_convergencia(historia_pf_13)
    #
    #graficar(graf_convergencia)
    graficar(graf_historia)
    graficar(graf_historia)

    print("Hallando raices de f1 por metodo brentq incluido en scipy.optimize")
    print(brentq(f1, 0, 2 * RADIO))

def raices_derivada():
    print("La raices de la derivada calculada con la calculadora del punto 2" + str(calcular_raices(math.pi,2*math.pi*RADIO,0,1e-7)))

if __name__ == "__main__":
    test_raices()
    raices_derivada()
