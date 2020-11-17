from sympy import *

from MetodosBusquedaRaices.Biseccion import biseccion


def newton_raphson_rec(f, f_prima, semilla, tolerancia, iteraciones):
    x = symbols('x')
    if abs(f(semilla)) <= tolerancia or iteraciones == 0:
        return semilla

    try:
        siguiente = semilla - f(semilla) / f_prima.evalf(subs={x: semilla})
    except ZeroDivisionError:
        print('El denominador resultó nulo para f\' en cierto punto, no se puede continuar, se devuelve último valor')
        return semilla

    return newton_raphson_rec(f, f_prima, siguiente, tolerancia, iteraciones - 1)


def newton_raphson(f, inicio, fin, tolerancia, iteraciones=-1):
    x = symbols('x')
    f_prima = f(x).diff(x)
    # tal vez el numero de iteraciones para hallar la semilla se podria determinar dinamicamente
    semilla = biseccion(f, inicio, fin, tolerancia, 5)
    print('la semilla inicial fue' + str(semilla))
    return newton_raphson_rec(f, f_prima, semilla, tolerancia, iteraciones)


def f_test_lineal(x):
    return x - 4


def f_test_logaritmica(x):
    return log(x)


def f_test_pol(x):
    return x ** 2 - 4 * x - 5

def test_nr():
    print(biseccion(f_test_lineal, 0.1, 20, 0.001))
    print(newton_raphson(f_test_lineal, 0.1, 20, 0.001))
    print(newton_raphson(f_test_pol, 0.1, 20, 0.001))
    print(newton_raphson(f_test_logaritmica, 0.1, 20, 0.001))
