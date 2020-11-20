from sympy import *
from TP1.MetodosBusquedaRaices.Biseccion import biseccion
import numpy

MAXIT = 50


def newton_raphson_mod_rec(f, f_prima, f_prima_prima, semilla, tolerancia, iteraciones, historia, it_actual):
    x = symbols('x')
    if abs(f(semilla)) <= tolerancia or iteraciones == 0:
        historia = historia[:it_actual]
        return semilla, historia, it_actual

    fp = lambdify(x, f_prima)
    fpp = lambdify(x, f_prima_prima)

    try:
        siguiente = semilla - f(semilla) * fp(semilla) / (fp(semilla) ** 2 - f(semilla) * fpp(semilla))
        historia[it_actual] = (it_actual, siguiente)

    except ZeroDivisionError:
        print('El denominador resultó nulo para NRM en cierto punto, no se puede continuar, se devuelve último valor')
        return semilla, historia, it_actual

    return newton_raphson_mod_rec(f, f_prima, f_prima_prima, siguiente, tolerancia, iteraciones - 1, historia, it_actual + 1)


def newton_raphson_mod(f, intervalo, tolerancia, iteraciones=-1):
    x = symbols('x')
    f_prima = f(x).diff(x)
    f_prima_prima = f(x).diff(x, 2)
    # tal vez el numero de iteraciones para hallar la semilla se podria determinar dinamicamente
    semilla, _, _ = biseccion(f, (intervalo[0], intervalo[1]), tolerancia, 1)
    historia = numpy.zeros((MAXIT, 2))
    return newton_raphson_mod_rec(f, f_prima, f_prima_prima, semilla, tolerancia, iteraciones, historia, 0)

