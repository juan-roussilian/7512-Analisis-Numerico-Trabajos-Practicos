from sympy import *

from TP1.MetodosBusquedaRaices.Biseccion  import biseccion


def secante_rec(f, primer_semilla, segunda_semilla, tolerancia, iteraciones):
    if abs(f(segunda_semilla)) <= tolerancia or iteraciones == 0:
        return segunda_semilla

    try:
        actual = segunda_semilla
        segunda_semilla = actual - (f(actual) * (actual - primer_semilla)) / (f(actual) - f(primer_semilla))
        primer_semilla = actual
    except ZeroDivisionError:
        print('El denominador resultó nulo para f\' en cierto punto, no se puede continuar, se devuelve último valor')
        return segunda_semilla

    return secante_rec(f, primer_semilla, segunda_semilla, tolerancia, iteraciones - 1)


def secante(f, inicio, fin, tolerancia, iteraciones=-1):
    # tal vez el numero de iteraciones para hallar la semilla se podria determinar dinamicamente
    primer_semilla = biseccion(f, inicio, fin, tolerancia, 5)
    segunda_semilla = biseccion(f, inicio, fin, tolerancia, 6)
    return secante_rec(f, primer_semilla, segunda_semilla, tolerancia, iteraciones)


def f_test_lineal(x):
    return x - 4


def f_test_logaritmica(x):
    return log(x)


def f_test_pol(x):
    return x ** 2 - 4 * x - 5


def test_secante():
    print(biseccion(f_test_lineal, 0.1, 20, 0.001))
    print(secante(f_test_lineal, 0.1, 20, 0.001))
    print(secante(f_test_pol, 0.1, 1000, 0.001))
    print(secante(f_test_logaritmica, 0.1, 20, 0.001))
