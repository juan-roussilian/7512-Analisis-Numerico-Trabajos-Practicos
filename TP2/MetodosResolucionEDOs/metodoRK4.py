import numpy as np
from TP1.MetodosBusquedaRaices.RepresentacionHistorias import graficar


# primera ecuación diferencial del sistema depredador-presa
def f_dif(a, b):
    return lambda x, y: a * x - b * x * y


# segunda ecuación diferencial del sistema depredador-presa
def g_dif(c, d):
    return lambda x, y: c * x * y - d * y


# metodo RK-4
def rk4(x0, y0, h, ti, tf, f, g):
    iteraciones = int((tf - ti) / h) + 1

    historia_x = np.zeros((iteraciones, 2))
    historia_y = np.zeros((iteraciones, 2))
    estado_espacio = np.zeros((iteraciones, 2))

    print('\n--------SOLUTION--------')
    print('-------------------------')
    print('x0\ty0')
    print('-------------------------')

    for i in range(iteraciones):
        historia_x[i] = (ti, x0)
        historia_y[i] = (ti, y0)
        estado_espacio[i] = (x0, y0)

        m1 = f(x0, y0)
        k1 = g(x0, y0)

        m2 = f((x0 + h * m1 / 2), (y0 + h * k1 / 2))
        k2 = g((x0 + h * m1 / 2), (y0 + h * k1 / 2))

        m3 = f((x0 + h * m2 / 2), (y0 + h * k2 / 2))
        k3 = g((x0 + h * m2 / 2), (y0 + h * k2 / 2))

        m4 = f((x0 + h * m3), (y0 + h * k3))
        k4 = g((x0 + h * m3), (y0 + h * k3))

        k = (k1 + 2 * k2 + 2 * k3 + k4) * (h / 6)
        m = (m1 + 2 * m2 + 2 * m3 + m4) * (h / 6)

        print('%.4f\t%.4f' % (x0, y0))
        print('-------------------------')

        # a cual le sumo cual????
        y0 = y0 + k
        x0 = x0 + m

        ti = ti + h

    return {'Presas': historia_x, 'Depredadores': historia_y, 'Estado_Espacio': estado_espacio}


if __name__ == "__main__":
    print('Ingrese las condiciones iniciales:')
    x_inicial = float(input('x0 = '))
    y_inicial = float(input('y0 = '))

    print('Ingrese la razón de crecimiento de las presas:')
    crecimiento_presa = float(input('a = '))

    print('Ingrese los parámetros de la interacción para la muerte de presas:')
    muerte_presas = float(input('b = '))

    print('Ingrese la razón de muerte de los depredadores:')
    muerte_depredadores = float(input('c = '))

    print('Ingrese los parámetros de la interacción para el crecimiento del depredador:')
    crecimiento_depredadores = float(input('d = '))

    funcion_f = f_dif(crecimiento_presa, muerte_presas)
    funcion_g = g_dif(muerte_depredadores, crecimiento_depredadores)

    print(funcion_f)
    print(funcion_g)

    print('Ingrese el incremento de cada paso:')
    h_incremento = float(input('h = '))

    print('Ingrese el tiempo inicial')
    t_inicial = float(input('ti= '))

    print('Ingrese el tiempo final')
    t_final = float(input('tf= '))

    # llamo al metodo
    historias_graficos = rk4(x_inicial, y_inicial, h_incremento, t_inicial, t_final, funcion_f, funcion_g)

    # reutilizamos el mismo graficador del TP1 \(★ω★)/
    graficar(historias_graficos, "aaa", "eee")
