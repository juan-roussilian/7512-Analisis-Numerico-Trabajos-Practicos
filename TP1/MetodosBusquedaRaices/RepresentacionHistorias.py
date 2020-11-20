from matplotlib import pyplot as plt
from tabulate import tabulate
import numpy

MAXTABLA = 12


def tabular_historia(historia, nombre_tabla, it_totales):
    print("Tabulando método " + nombre_tabla)
    print("Se llegó a la tolerancia buscada en " + str(it_totales) + " iteraciones \n")

    encabezados = ['Iteracion', 'Aproximacion']
    iteraciones = [*range(1, it_totales+1)]
    aux = [x[1] for x in historia]
    tabla = zip(iteraciones, aux)

    print(tabulate(tabla, headers=encabezados, floatfmt=".16f"))
    print("La estimación final por el método " + nombre_tabla + " de la raíz fue" + str(aux[it_totales - 1]))


def graficar(diccionario_historia):
    plt.title("Comparación entre métodos de búsqueda de raíces")
    plt.ylabel('Estimacion raiz [n]')
    plt.xlabel('Iteracion [n]')
    plt.grid(True)
    plt.legend(loc='best')
    plt.show()
    plt.figure()
    for metodo in diccionario_historia:
        historia = diccionario_historia[metodo]
        print(historia)
        plt.plot(historia[:, 0], historia[:,1], '-', lw=2, label=metodo)
