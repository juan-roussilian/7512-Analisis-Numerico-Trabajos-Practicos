import math
import numpy

MAXIT = 50


def biseccion_rec(f, inicio, fin, tolerancia, iteraciones, historia, it_actual):
    mitad = (inicio + fin) / 2
    historia[it_actual] = (it_actual, mitad)

    if (abs(f(mitad)) <= tolerancia) or iteraciones == 0:
        historia = historia[:it_actual + 1]
        return mitad, historia, it_actual + 1
    if f(mitad) * f(inicio) >= 0:
        inicio = mitad
    elif f(mitad) * f(fin) >= 0:
        fin = mitad
    return biseccion_rec(f, inicio, fin, tolerancia, iteraciones - 1, historia, it_actual + 1)


# recibe opcionalmente un parámetro de iteraciones, por default es -1 para no cortar la bisección prematuramente.
def biseccion(f, intervalo, tolerancia, iteraciones=-1):
    historia = numpy.zeros((MAXIT,2))
    it_actual = 0
    if f(intervalo[0]) * f(intervalo[1]) >= 0:
        print("Imposible aplicar bisección")
        return None, None, None
    return biseccion_rec(f, intervalo[0], intervalo[1], tolerancia, iteraciones - 1, historia, it_actual)

