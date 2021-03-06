import numpy as np

# Metodo RK-4
def rk4(x0, y0, h, ti, tf, f, g):
    iteraciones = int((tf - ti) / h) + 1

    historia_x = np.zeros((iteraciones, 2))
    historia_y = np.zeros((iteraciones, 2))
    estado_espacio = np.zeros((iteraciones, 2))

    print('\n--------SOLUCION--------')
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

        y0 = y0 + k
        x0 = x0 + m

        ti = ti + h

    return {'Presas': historia_x, 'Depredadores': historia_y, 'Estado_Espacio': estado_espacio}

