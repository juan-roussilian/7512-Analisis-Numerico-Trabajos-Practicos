import math

from TP1.MetodosBusquedaRaices.Biseccion import biseccion
from TP1.MetodosBusquedaRaices.NewtonRaphson import newton_raphson
from TP1.MetodosBusquedaRaices.PuntoFijo import punto_fijo
from TP1.MetodosBusquedaRaices.Secante import secante

RADIO = 4.25


def f1(x):
    return 4.25 * math.pi * x ** 2 - (math.pi * x ** 3) / 3 - 180.52


def test_raices():
    print("Hallando raices de f1 por metodo de Bisección con tolerancia 1e-5")
    print(biseccion(f1, (RADIO, 2 * RADIO), 1e-5))
    print("Hallando raices de f1 por metodo de Bisección con tolerancia 1e-13")
    print(biseccion(f1, (RADIO, 2 * RADIO), 1e-13))

    print("Hallando raices de f1 por metodo de NR con tolerancia 1e-5")
    print(newton_raphson(f1, (RADIO, 2 * RADIO), 1e-5))
    print("Hallando raices de f1 por metodo de NR con tolerancia 1e-13")
    print(newton_raphson(f1, (RADIO, 2 * RADIO), 1e-13))

    print("Hallando raices de f1 por metodo de secante con tolerancia 1e-5")
    print(secante(f1, (RADIO, 2 * RADIO), 1e-5))
    print("Hallando raices de f1 por metodo de secante con tolerancia 1e-13")
    print(secante(f1, (RADIO, 2 * RADIO), 1e-13))

    print("Hallando raices de f1 por metodo de punto fijo con tolerancia 1e-5")
    print(punto_fijo("4.25 * pi * x ** 2 - (pi * x ** 3) / 3 - 180.52", (RADIO, 6), 1e-5, 200))
    print("Hallando raices de f1 por metodo de punto fijo con tolerancia 1e-13")
    print(punto_fijo("4.25 * pi * x ** 2 - (pi * x ** 3) / 3 - 180.52", (RADIO, 6), 1e-13, 200))
