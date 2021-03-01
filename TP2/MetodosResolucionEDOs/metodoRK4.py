# RK-4 method python program

# function to be solved
def f(x, y, a, b):
    return a * x + b * x * y


def g(x, y, c, d):
    return c * x * y - d * y


# or
# f = lambda x: x+y

# RK-4 method
def rk4(x0, y0, xn, ti, tf):
    # Calculating step size
    h = 0.1

    print('\n--------SOLUTION--------')
    print('-------------------------')
    print('x0\ty0\tyn')
    print('-------------------------')

    # falta mandar a,b,c,d en cada llamada a las funciones g y f.
    # Creo que lo mejor sería tener funciones que reciban a,b,c,d de parámetro y devuelvan expresiones lambda ya
    # formadas con esos params.

    while ti < tf:
        k1 = (f(x0, y0))
        k2 = (f((x0 + h / 2), (y0 + k1 / 2)))
        k3 = (f((x0 + h / 2), (y0 + k2 / 2)))
        k4 = (f((x0 + h), (y0 + k3)))
        k = (k1 + 2 * k2 + 2 * k3 + k4) * (h / 6)

        m1 = (g(x0, y0))
        m2 = (g((x0 + h / 2), (y0 + m1 / 2)))
        m3 = (g((x0 + h / 2), (y0 + m2 / 2)))
        m4 = (g((x0 + h), (y0 + m3)))
        m = (m1 + 2 * m2 + 2 * m3 + m4) * (h / 6)

        yn = y0 + k
        xn = x0 + m

        # print('%.4f\t%.4f\t%.4f' % (x0, y0, yn))
        # print('-------------------------')
        y0 = yn
        x0 = xn
        ti = ti + h

    # print('\nAt x=%.4f, y=%.4f' % (xn, yn))


# Inputs
print('Enter initial conditions:')
x0 = float(input('x0 = '))
y0 = float(input('y0 = '))

print('Enter calculation point: ')
xn = float(input('xn = '))

print('Enter number of steps:')
step = int(input('Number of steps = '))

# RK4 method call
rk4(x0, y0, xn, step)
