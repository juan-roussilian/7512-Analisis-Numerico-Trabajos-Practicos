from TP1.MetodosBusquedaRaices.PuntoFijo import *


def punto_fijo(g, intervalo, tolerancia, iteraciones=-1):

    if(existe_unico_p_fijo(g,symbols('x'),intervalo)):
        semilla = biseccion(lambdify(symbols('x'), g), intervalo, tolerancia, 3)
        print("La raiz hallada como semilla es: " + str(semilla))
        return punto_fijo_rec(lambdify(symbols('x'),g), semilla, tolerancia, iteraciones)
    else:
        return "No es posible aplicar punto fijo dada la falta de existencia y/o unicidad del punto fijo"
