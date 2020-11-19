from matplotlib import pyplot as plt
from tabulate import tabulate

MAXTABLA = 12


def recortar_historia(hist):
    aux = hist[:6] + hist[-6:]
    print(len(aux))
    return aux


def tabular_historia(historia, nombre_tabla):
    print(len(historia))
    if len(historia) > MAXTABLA:
        historia = recortar_historia(historia)

    print("Tabulando método " + nombre_tabla + "\n")

    header = ['Iteracion', 'Aproximacion']
    iteraciones = range(1, len(historia) + 1)
    table = zip(iteraciones, historia)

    print(tabulate(table, headers=header))


def graficar_historias(diccionario_metodos_raices):
    #    cantidad_iteraciones = len(lista_iteraciones) + 1
    plt.title("Comparación entre métodos de búsqueda de raíces")
    plt.xlabel('Paso [n]')
    plt.grid(True)
    plt.legend(loc='best')
    plt.show()
    plt.figure()

    for metodo in diccionario_metodos_raices:
        historia = recortar_historia(diccionario_metodos_raices[metodo])
        plt.plot(range(MAXTABLA), historia, '-', lw=2, label=metodo)
