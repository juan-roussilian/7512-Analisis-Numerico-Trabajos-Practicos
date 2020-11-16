import math


def biseccion_rec(f, inicio, fin, tolerancia, iteraciones):
    mitad = (inicio + fin) / 2
    if (abs(f(mitad)) <= tolerancia) or iteraciones == 0:
        return mitad
    if f(mitad) * f(inicio) >= 0:
        inicio = mitad
    elif f(mitad) * f(fin) >= 0:
        fin = mitad
    return biseccion_rec(f, inicio, fin, tolerancia, iteraciones - 1)


# recibe opcionalmente un parámetro de iteraciones, por default es -1 para no cortar la bisección prematuramente.
def biseccion(f, inicio, fin, tolerancia, iteraciones=-1):
    if f(inicio) * f(fin) >= 0:
        print("Imposible aplicar bisección")
    if iteraciones == 0:
        print("numero invalido de iteraciones")
    return biseccion_rec(f, inicio, fin, tolerancia, iteraciones - 1)
