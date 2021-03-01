# RK-4 method python program

# function to be solved

# primera ecuación diferencial del sistema depredador-presa
def f_dif(a, b):
    return lambda x, y: a * x + b * x * y


# segunda ecuación diferencial del sistema depredador-presa
def g_dif(c, d):
    return lambda x, y: c * x * y - d * y


# RK-4 method
def rk4(x0, y0, h, ti, tf, f, g):
    # Calculating step size

    print('\n--------SOLUTION--------')
    print('-------------------------')
    print('x0\ty0\txn\tyn')
    print('-------------------------')

    while ti < tf:
        k1 = f(x0, y0)
        k2 = f((x0 + h / 2), (y0 + k1 / 2))
        k3 = f((x0 + h / 2), (y0 + k2 / 2))
        k4 = f((x0 + h), (y0 + k3))
        k = (k1 + 2 * k2 + 2 * k3 + k4) * (h / 6)

        m1 = g(x0, y0)
        m2 = g((x0 + h / 2), (y0 + m1 / 2))
        m3 = g((x0 + h / 2), (y0 + m2 / 2))
        m4 = g((x0 + h), (y0 + m3))
        m = (m1 + 2 * m2 + 2 * m3 + m4) * (h / 6)

        yn = y0 + k
        xn = x0 + m

        print('%.4f\t%.4f\t%.4f\t%.4f' % (x0, y0, xn, yn))
        print('-------------------------')

        y0 = yn
        x0 = xn
        ti = ti + h

    # print('\nAt x=%.4f, y=%.4f' % (xn, yn))


# Inputs
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

    print('Ingrese el incremento de cada paso:')
    h_incremento = float(input('h = '))

    print('Ingrese el tiempo inicial')
    t_inicial = float(input('ti= '))

    print('Ingrese el tiempo final')
    t_final = float(input('tf= '))

    funcion_f = f_dif(crecimiento_presa, muerte_presas)
    funcion_g = g_dif(muerte_depredadores, crecimiento_depredadores)

    # RK4 method call
    rk4(x_inicial, y_inicial, h_incremento, t_inicial, t_final, funcion_f, funcion_g)
