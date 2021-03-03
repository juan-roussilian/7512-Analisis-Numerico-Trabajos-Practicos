from TP1.MetodosBusquedaRaices.RepresentacionHistorias import graficar
from TP2.MetodosResolucionEDOs.metodoRK4 import rk4

# primera ecuación diferencial del sistema depredador-presa


def f_dif(a, b):
    return lambda x, y: a * x - b * x * y


# segunda ecuación diferencial del sistema depredador-presa
def g_dif(c, d):
    return lambda x, y: c * x * y - d * y

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