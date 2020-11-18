from TP1.MetodosBusquedaRaices.Biseccion import biseccion
import numpy as np
from sympy import *
import math

def x(x):
    return x

def punto_fijo_rec(g, semilla, tolerancia, iteraciones):
    if abs(g(semilla)) <= tolerancia or iteraciones == 0:
        return semilla
    return punto_fijo_rec(g, g(semilla), tolerancia, iteraciones - 1)

def obtener_g(f):
    x = symbols('x')
    expresion = x - sympify(f)
    return lambdify(x, expresion)


def punto_fijo(f, intervalo, tolerancia, iteraciones):

    g = obtener_g(f)
    semilla = biseccion(g, intervalo, tolerancia,2)
    print("La raiz hallada como semilla es: " + str(semilla))
    return punto_fijo_rec(g, semilla, tolerancia, iteraciones)

def existe_unico_p_fijo(g, intervalo):
    g_prima = g(symbols('x')).diff(x)
    return true

if __name__ == "__main__":

    print("la raiz hallaada con p fijo es: " +  str(punto_fijo("x ** 2 - 1", (0, 2), 1e-2, 200)))