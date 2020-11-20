from sympy import *
from TP1.MetodosBusquedaRaices.Biseccion import biseccion
import numpy

IT_BISECCION_SEMILLA = 1
MAXIT = 50

def newton_raphson_rec(f, f_prima, semilla, tolerancia, iteraciones, historia, it_actual):
    x = symbols('x')
    if abs(f(semilla)) <= tolerancia or iteraciones == 0:
        historia = historia[:it_actual]
        return semilla, historia, it_actual

    try:
        siguiente = semilla - f(semilla) / f_prima.evalf(subs={x: semilla})
        historia[it_actual] = (it_actual, siguiente)
    except ZeroDivisionError:
        print('El denominador resultó nulo para f\' en cierto punto, no se puede continuar, se devuelve último valor')
        return semilla, historia, it_actual

    return newton_raphson_rec(f, f_prima, siguiente, tolerancia, iteraciones - 1, historia, it_actual + 1)


def newton_raphson(f, intervalo, tolerancia, iteraciones=-1):
    x = symbols('x')
    f_prima = f(x).diff(x)
    historia = numpy.zeros((MAXIT,2))
    # tal vez el numero de iteraciones para hallar la semilla se podria determinar dinamicamente
    semilla, hist_bis, _ = biseccion(f, (intervalo[0], intervalo[1]), tolerancia, IT_BISECCION_SEMILLA)
    return newton_raphson_rec(f, f_prima, semilla, tolerancia, iteraciones, historia, 0)
