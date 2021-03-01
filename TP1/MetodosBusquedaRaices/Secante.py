from sympy import *
import numpy
from TP1.MetodosBusquedaRaices.Biseccion import biseccion

MAXIT = 50

def secante_rec(f, primer_semilla, segunda_semilla, tolerancia, iteraciones, historia, it_actual):
    if abs(f(segunda_semilla)) <= tolerancia or iteraciones == 0:
        historia = historia[:it_actual]
        return segunda_semilla, historia, it_actual

    try:
        actual = segunda_semilla
        segunda_semilla = actual - (f(actual) * (actual - primer_semilla)) / (f(actual) - f(primer_semilla))
        primer_semilla = actual
        historia[it_actual] = (it_actual, segunda_semilla)
    except ZeroDivisionError:
        print('El denominador resultó nulo para f\' en cierto punto, no se puede continuar, se devuelve último valor')
        return segunda_semilla, historia, it_actual

    return secante_rec(f, primer_semilla, segunda_semilla, tolerancia, iteraciones - 1, historia, it_actual + 1)


def secante(f, intervalo, tolerancia, iteraciones=-1):
    # tal vez el numero de iteraciones para hallar la semilla se podria determinar dinamicamente
    primer_semilla, _, _ = biseccion(f, intervalo, tolerancia, 1)
    segunda_semilla, _, _ = biseccion(f, intervalo, tolerancia, 2)
    historia = numpy.zeros((MAXIT, 2))
    it_actual = 0
    return secante_rec(f, primer_semilla, segunda_semilla, tolerancia, iteraciones, historia, it_actual)

