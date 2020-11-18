from TP1.MetodosBusquedaRaices.Biseccion import biseccion
import numpy as np
from sympy import *
import math

def x(x):
    return x

def punto_fijo_rec(g, semilla, tolerancia, iteraciones):
    return

def obtener_g(f):

    x = symbols('x')
    expresion = x - sympify(str(f()))
    return lambdify(x, expresion)


def punto_fijo(f,intervalo, tolerancia, iteraciones):

    g = obtener_g(f)
    semilla = biseccion(g, intervalo,tolerancia, iteraciones)

    return punto_fijo_rec(g, semilla, tolerancia, iteraciones)

def existe_unico_p_fijo(g, intervalo):
    g_prima = g(symbols('x')).diff(x)

def lineal(x):
    return  x/2

if __name__ == "__main__":

    punto_fijo(lineal, (0,1), 1e-2, 2)