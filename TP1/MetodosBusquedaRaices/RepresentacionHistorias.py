from matplotlib import pyplot as plt
from tabulate import tabulate

MAXTABLA = 12


def recortar_historia(hist):
    aux = hist[:6] + hist[-6:]
    return aux


def tabular_historia(historia, nombre_tabla):
    it_totales = len(historia)
    print(it_totales)
    corte = 7
    if len(historia) > MAXTABLA:
        corte = len(historia) - 5
        historia = recortar_historia(historia)

    print("Tabulando método " + nombre_tabla + "\n")

    encabezados = ['Iteracion', 'Aproximacion']
    iteraciones = [*range(1, 7)] + [*range(corte, it_totales + 1)]
    tabla = zip(iteraciones, historia)

    print(tabulate(tabla, headers=encabezados, floatfmt=".16f"))


def graficar(diccionario_historia):
    plt.title("Comparación entre métodos de búsqueda de raíces")
    plt.ylabel('Estimacion raiz [n]')
    plt.xlabel('Iteracion [n]')
    plt.grid(True)
    plt.legend(loc='best')
    plt.show()
    plt.figure()

    for metodo in diccionario_historia:
        historia = recortar_historia(diccionario_historia[metodo])
        plt.plot(range(MAXTABLA), historia, '-', lw=2, label=metodo)
