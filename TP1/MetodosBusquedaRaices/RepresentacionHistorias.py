from matplotlib import pyplot as plt
from tabulate import tabulate

MAXTABLA = 12


def recortar_historia(hist):
    return hist[:MAXTABLA / 2] + hist[MAXTABLA / 2:]


def tabular_historia(historia, nombre_tabla):
    if len(historia) > MAXTABLA:
        historia = recortar_historia(historia)

    print("Tabulando método" + nombre_tabla)

    header = ['Iteracion' 'Aproximacion']
    iteraciones = range(len(historia))
    table = zip(iteraciones, historia)

    print(tabulate(table, headers=header, floatfmt=".4f"))


def graficar_historias(diccionario_metodos_raices):
    #    cantidad_iteraciones = len(lista_iteraciones) + 1
    plt.title("Comparación entre métodos de búsqueda de raíces")
    plt.xlabel('Paso [n]')
    plt.grid(True)
    plt.legend(loc='best')
    plt.show()
    plt.figure()

    for metodo in diccionario_metodos_raices:
        historia = diccionario_metodos_raices[metodo]
        plt.plot(historia[:, 1], historia[:, 1], '-', lw=2, label=metodo)
