from TP1.MetodosBusquedaRaices.RepresentacionHistorias import graficar
from TP2.MetodosResolucionEDOs.metodoRK4 import rk4

# primera ecuación diferencial del sistema depredador-presa


def f_dif(a, b):
    return lambda x, y: a * x - b * x * y


# segunda ecuación diferencial del sistema depredador-presa
def g_dif(c, d):
    return lambda x, y: c * x * y - d * y

def pedir_input_numerico(nombreParametro):
    input_es_valido = False
    input_usuario = None
    while(not input_es_valido):
        try:
            input_usuario = float(input(nombreParametro +' = '))
            input_es_valido = True
        except ValueError:
            print('No se ingreso un valor numerico')
    return input_usuario

def pedir_respuesta_afirmativa_negativa():
    input_es_valido = False
    input_usuario = None
    while (not input_es_valido):
            input_usuario = input('S/N ')
            if(input_usuario == 'S' or input_usuario == 'N'):
                input_es_valido = True
            else:
                print('Comando no valido')
    return input_usuario


if __name__ == "__main__":

    print('Desea realizar la simulacion con los parametros del item A?')

    if(pedir_respuesta_afirmativa_negativa() == 'S'):
        x_inicial=2
        y_inicial=1
        crecimiento_presa=1.2
        muerte_presas=0.6
        muerte_depredadores=0.3
        crecimiento_depredadores=0.8
        h_incremento=0.1
        t_inicial=0
        t_final=30

    else:
        print('Ingrese las condiciones iniciales:')
        x_inicial = pedir_input_numerico('x0')
        y_inicial = pedir_input_numerico('y0')

        print('Ingrese la razón de crecimiento de las presas:')
        crecimiento_presa = float(input('a = '))

        print('Ingrese los parámetros de la interacción para la muerte de presas:')
        muerte_presas = pedir_input_numerico('b')

        print('Ingrese la razón de muerte de los depredadores:')
        muerte_depredadores = pedir_input_numerico('c')

        print('Ingrese los parámetros de la interacción para el crecimiento del depredador:')
        crecimiento_depredadores = pedir_input_numerico('d')

        print('Ingrese el incremento de cada paso:')
        h_incremento = pedir_input_numerico('h')

        print('Ingrese el tiempo inicial')
        t_inicial = pedir_input_numerico('ti')

        print('Ingrese el tiempo final')
        t_final = pedir_input_numerico('tf')

    # Creo las funciones en base a los parametros
    funcion_f = f_dif(crecimiento_presa, muerte_presas)
    funcion_g = g_dif(muerte_depredadores, crecimiento_depredadores)

    # Llamo al metodo
    historias_graficos = rk4(x_inicial, y_inicial, h_incremento, t_inicial, t_final, funcion_f, funcion_g)

    # Separo el diccionario de historias por grafico, ya que el graficador requiere diccionarios de estas
    historias_presa_depredador = {x:historias_graficos[x] for x in ['Presas','Depredadores']}
    historia_estado_espacio = {x:historias_graficos[x] for x in ['Estado_Espacio']}

    # Reutilizamos el mismo graficador del TP1 \(★ω★)/
    graficar(historias_presa_depredador, 'Oscilacion presa-depredador', 'Numero de individuos', 'Tiempo')
    graficar(historia_estado_espacio,"Estado espacio","Depredadores", "Presas")