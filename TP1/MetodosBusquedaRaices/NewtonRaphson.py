from sympy import *
from TP1.MetodosBusquedaRaices.Biseccion import biseccion


def newton_raphson_rec(f, f_prima, semilla, tolerancia, iteraciones, historia):
    x = symbols('x')
    if abs(f(semilla)) <= tolerancia or iteraciones == 0:
        return semilla, historia

    try:
        siguiente = semilla - f(semilla) / f_prima.evalf(subs={x: semilla})
        historia.append(siguiente)

    except ZeroDivisionError:
        print('El denominador resultó nulo para f\' en cierto punto, no se puede continuar, se devuelve último valor')
        return semilla, historia

    return newton_raphson_rec(f, f_prima, siguiente, tolerancia, iteraciones - 1, historia)


def newton_raphson(f, intervalo, tolerancia, iteraciones=-1):
    x = symbols('x')
    f_prima = f(x).diff(x)
    # tal vez el numero de iteraciones para hallar la semilla se podria determinar dinamicamente
    semilla, historia  = biseccion(f, (intervalo[0], intervalo[1]), tolerancia, 2)
    return newton_raphson_rec(f, f_prima, semilla, tolerancia, iteraciones, historia)

