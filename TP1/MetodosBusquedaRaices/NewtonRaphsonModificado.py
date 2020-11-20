from sympy import *
from TP1.MetodosBusquedaRaices.Biseccion import biseccion


def newton_raphson_mod_rec(f, f_prima, f_prima_prima, semilla, tolerancia, iteraciones, historia):
    x = symbols('x')
    if abs(f(semilla)) <= tolerancia or iteraciones == 0:
        return semilla, historia

    fp = lambdify(x, f_prima)
    fpp = lambdify(x, f_prima_prima)

    try:
        siguiente = semilla - f(semilla) * fp(semilla) / (fp(semilla) ** 2 - f(semilla) * fpp(semilla))
        historia.append(siguiente)

    except ZeroDivisionError:
        print('El denominador resultó nulo para NRM en cierto punto, no se puede continuar, se devuelve último valor')
        return semilla, historia

    return newton_raphson_mod_rec(f, f_prima, f_prima_prima, siguiente, tolerancia, iteraciones - 1, historia)


def newton_raphson_mod(f, intervalo, tolerancia, iteraciones=-1):
    x = symbols('x')
    f_prima = f(x).diff(x)
    f_prima_prima = f(x).diff(x, 2)
    # tal vez el numero de iteraciones para hallar la semilla se podria determinar dinamicamente
    semilla, historia = biseccion(f, (intervalo[0], intervalo[1]), tolerancia, 5)
    return newton_raphson_mod_rec(f, f_prima, f_prima_prima, semilla, tolerancia, iteraciones, historia)

