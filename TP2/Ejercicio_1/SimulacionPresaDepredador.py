from TP1.MetodosBusquedaRaices.RepresentacionHistorias import graficar
from TP2.MetodosResolucionEDOs.metodoRK4 import rk4


def pedir_input_numerico(nombreParametro):
    input_es_valido = False
    input_usuario = None
    while not input_es_valido:
        try:
            input_usuario = float(input(nombreParametro + ' = '))
            input_es_valido = True
        except ValueError:
            print('No se ingreso un valor numerico')
    return input_usuario


def pedir_respuesta_afirmativa_negativa():
    input_es_valido = False
    input_usuario = None
    while not input_es_valido:
        input_usuario = input('S/N ')
        if input_usuario == 'S' or input_usuario == 'N':
            input_es_valido = True
        else:
            print('Comando no valido')
    return input_usuario


def pedir_comando():
    input_es_valido = False
    input_usuario = None
    while not input_es_valido:
        input_usuario = input('A/D/M ')
        if input_usuario == 'A' or input_usuario == 'D' or input_usuario == 'M':
            input_es_valido = True
        else:
            print('Comando no valido')
    return input_usuario


def obtener_parametros_item_a():
    parametros_item_a = {
        'x_inicial': 2,
        'y_inicial': 1,
        'crecimiento_presa': 1.2,
        'muerte_presas': 0.6,
        'crecimiento_depredadores': 0.8,
        'muerte_depredadores': 0.3,
        'h_incremento': 0.1,
        't_inicial': 0,
        't_final': 30
    }
    return parametros_item_a


def obtener_parametros_item_d():
    parametros_item_d = {
        'x_inicial': 2,
        'y_inicial': 1,
        'crecimiento_presa': 2.4,
        'muerte_presas': 1.2,
        'crecimiento_depredadores': 1.6,
        'muerte_depredadores': 0.6,
        'h_incremento': 0.1,
        't_inicial': 0,
        't_final': 30
    }
    return parametros_item_d


def f_dif(a, b):
    return lambda x, y: a * x - b * x * y


# segunda ecuación diferencial del sistema depredador-presa
def g_dif(c, d):
    return lambda x, y: c * x * y - d * y


if __name__ == "__main__":

    parametros = {}
    usuario_quiere_simular = True
    while usuario_quiere_simular:

        print('Desea realizar la simulacion con los parametros del item A, del item D, o con ' +
              'parametros manualmente cargados? (A/D/M)')
        comando_usuario = pedir_comando()

        if comando_usuario == 'A':
            parametros = obtener_parametros_item_a()

        elif comando_usuario == 'D':
            parametros = obtener_parametros_item_d()

        else:
            print('Ingrese las condiciones iniciales:')
            parametros['x_inicial'] = pedir_input_numerico('x0')
            parametros['y_inicial'] = pedir_input_numerico('y0')

            print('Ingrese la razón de crecimiento de las presas:')
            parametros['crecimiento_presa'] = pedir_input_numerico('a')

            print('Ingrese los parámetros de la interacción para la muerte de presas:')
            parametros['muerte_presas'] = pedir_input_numerico('b')

            print('Ingrese la razón de muerte de los depredadores:')
            parametros['muerte_depredadores'] = pedir_input_numerico('c')

            print('Ingrese los parámetros de la interacción para el crecimiento del depredador:')
            parametros['crecimiento_depredadores'] = pedir_input_numerico('d')

            print('Ingrese el incremento de cada paso:')
            parametros['h_incremento'] = pedir_input_numerico('h')

            print('Ingrese el tiempo inicial')
            parametros['t_inicial'] = pedir_input_numerico('ti')

            print('Ingrese el tiempo final')
            parametros['t_final'] = pedir_input_numerico('tf')

        # Creo las funciones en base a los parametros
        funcion_f = f_dif(parametros['crecimiento_presa'], parametros['muerte_presas'])
        funcion_g = g_dif(parametros['muerte_depredadores'], parametros['crecimiento_depredadores'])

        # Llamo al metodo
        historias_graficos = rk4(
            parametros['x_inicial'],
            parametros['y_inicial'],
            parametros['h_incremento'],
            parametros['t_inicial'],
            parametros['t_final'],
            funcion_f,
            funcion_g
        )

        # Separo el diccionario de historias por grafico, ya que el graficador requiere diccionarios de estas
        historias_presa_depredador = {x: historias_graficos[x] for x in ['Presas', 'Depredadores']}
        historia_estado_espacio = {x: historias_graficos[x] for x in ['Estado_Espacio']}

        # Reutilizamos el mismo graficador del TP1 \(★ω★)/
        graficar(historias_presa_depredador, 'Oscilacion presa-depredador', 'Numero de individuos', 'Tiempo')
        graficar(historia_estado_espacio, "Estado espacio", "Depredadores", "Presas")

        print('Seguir simulando?')
        if pedir_respuesta_afirmativa_negativa() == 'N':
            usuario_quiere_simular = False
