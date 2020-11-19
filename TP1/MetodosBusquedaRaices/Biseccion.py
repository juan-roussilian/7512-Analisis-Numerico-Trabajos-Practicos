import math


def biseccion_rec(f, inicio, fin, tolerancia, iteraciones, historia):
    mitad = (inicio + fin) / 2
    historia.append(mitad)

    if (abs(f(mitad)) <= tolerancia) or iteraciones == 0:
        return mitad, historia
    if f(mitad) * f(inicio) >= 0:
        inicio = mitad
    elif f(mitad) * f(fin) >= 0:
        fin = mitad
    return biseccion_rec(f, inicio, fin, tolerancia, iteraciones - 1, historia)


# recibe opcionalmente un parámetro de iteraciones, por default es -1 para no cortar la bisección prematuramente.
def biseccion(f, intervalo, tolerancia, iteraciones=-1):
    historia = []
    if f(intervalo[0]) * f(intervalo[1]) >= 0:
        print("Imposible aplicar bisección")
        return None
    return biseccion_rec(f, intervalo[0], intervalo[1], tolerancia, iteraciones - 1, historia)


def f_test_lineal(x):
    return x - 4


def f_test_logaritmica(x):
    return math.log(x)


def test_biseccion():
    print(biseccion(f_test_lineal, (2, 20), 0.01))
    print(biseccion(f_test_logaritmica, (0.1, 20), 0.01))
