from sympy import *

from TP1.MetodosBusquedaRaices.Biseccion import biseccion


def secante_rec(f, primer_semilla, segunda_semilla, tolerancia, iteraciones, historia):
    if abs(f(segunda_semilla)) <= tolerancia or iteraciones == 0:
        return segunda_semilla, historia

    try:
        actual = segunda_semilla
        segunda_semilla = actual - (f(actual) * (actual - primer_semilla)) / (f(actual) - f(primer_semilla))
        historia.append(segunda_semilla)
        primer_semilla = actual
    except ZeroDivisionError:
        print('El denominador resultó nulo para f\' en cierto punto, no se puede continuar, se devuelve último valor')
        return segunda_semilla, historia

    return secante_rec(f, primer_semilla, segunda_semilla, tolerancia, iteraciones - 1, historia)


def secante(f, intervalo, tolerancia, iteraciones=-1):
    # tal vez el numero de iteraciones para hallar la semilla se podria determinar dinamicamente
    primer_semilla, hist_aux_1 = biseccion(f, intervalo, tolerancia, 1)
    segunda_semilla, hist_aux_2 = biseccion(f, intervalo, tolerancia, 2)
    historia = [hist_aux_1[len(hist_aux_1) - 1]]
    return secante_rec(f, primer_semilla, segunda_semilla, tolerancia, iteraciones, historia)

