from matplotlib import pyplot as plt
from tabulate import tabulate
import numpy

MAXTABLA = 12


def tabular_historia_precision13(historia, nombre_tabla, it_totales):
    print("Tabulando método " + nombre_tabla)
    print("Se llegó a la tolerancia buscada en " + str(it_totales) + " iteraciones \n")

    encabezados = ['Iteracion', 'Aproximacion']
    iteraciones = [*range(1, it_totales + 2)]
    aux = [x[1] for x in historia]
    tabla = zip(iteraciones, aux)

    print(tabulate(tabla, headers=encabezados, floatfmt=".13f"))
    print("La estimación final por el método " + nombre_tabla + " de la raíz fue" + "%.13f" % aux[
        it_totales - 1] + "\n\n\n")


def tabular_historia_precision5(historia, nombre_tabla, it_totales):
    print("Tabulando método " + nombre_tabla)
    print("Se llegó a la tolerancia buscada en " + str(it_totales) + " iteraciones \n")

    encabezados = ['Iteracion', 'Aproximacion']
    iteraciones = [*range(1, it_totales + 2)]
    aux = [x[1] for x in historia]
    tabla = zip(iteraciones, aux)

    print(tabulate(tabla, headers=encabezados, floatfmt=".5f"))
    print("La estimación final por el método " + nombre_tabla + " de la raíz fue" + "%.5f" % aux[
        it_totales - 1] + "\n\n\n")


def graficar(diccionario_historia, titulo, label_eje_y, escala_y="linear"):
    plt.yscale(escala_y)
    i = 1
    estilo_linea = 'dashed'
    for metodo in diccionario_historia:
        if(i == 2 or i == 4 ):
            estilo_linea = 'dotted'

        historia = diccionario_historia[metodo]
        plt.plot(historia[:, 0], historia[:, 1], ls=estilo_linea, lw=2, label=metodo)
        i += 1
        estilo_linea = 'dashed'

    plt.title(titulo)
    plt.ylabel(label_eje_y)
    plt.xlabel('Iteracion [n]')
    plt.grid(True)
    plt.legend(loc='best')
    plt.figure()
    plt.show()