from sympy import *
import math


# Debe recibir una funcion dada en expresion de simpy, con variable x
def funcion_es_continua_en_intervalo(f, variable_ppal, intervalo, distancia_entre_x):

    es_continua = true

    i = intervalo[0]

    while (i <= intervalo[1]):

        limite_der = limit(f, variable_ppal, i, '+')
        limite_izq = limit(f, variable_ppal, i, '-')
        f_evaluable = lambdify(symbols('x'),f)
        f_evaluada = f_evaluable(i)
        limite  = limit(f, variable_ppal, i)
        cond_1 = abs(limite_der.evalf() - limite_izq.evalf())
        cond_2 = abs(f_evaluada - limite.evalf())

        if( cond_1 > 1e-10 or cond_2 > 1e-10 ):
            es_continua = false

        i += distancia_entre_x

    return es_continua

def funcion_contenida_intervalo(g, variable_ppal, intervalo, distancia_entre_x):
    i = intervalo[0]
    g_evaluable = lambdify(variable_ppal, g)
    esta_contenida = true
    while i <= intervalo[1]:

        if(g_evaluable(i) <  intervalo[0] or g_evaluable(i) > intervalo[1]):
            esta_contenida = false
            break
        i += distancia_entre_x

    return esta_contenida

def derivada_acotada_en_intervalo(g, variable_ppal, intervalo, distancia_entre_x):
    esta_acotada = true
    g_prima = g.diff(variable_ppal)
    g_prima_evaluabe = lambdify(variable_ppal,g_prima)
    i = intervalo[0]
    cota_mayor = - math.inf
    cota_menor = math.inf

    while i <= intervalo[1]:
        valor = g_prima_evaluabe(i)
        if(valor > cota_mayor):
            cota_mayor = valor
        if(valor < cota_menor):
            cota_menor = valor
        if( max(abs(cota_menor), abs(cota_mayor)) > 1 or min(abs(cota_menor), abs(cota_mayor) ) < 0  ):
            esta_acotada = false
            break
        i += distancia_entre_x

    return esta_acotada

def existe_unico_p_fijo(g, variable_ppal, intervalo):

    if (funcion_es_continua_en_intervalo(g, variable_ppal, intervalo, 1) and
        funcion_contenida_intervalo(g, variable_ppal, intervalo, 1) and
        derivada_acotada_en_intervalo(g, variable_ppal, intervalo, 1)
    ):
        return true
    else:
        return false

def obtener_g(f):
    x = symbols('x')
    expresion = x - (sympify(f)/100)
    return expresion

def punto_fijo_rec(g, f, semilla, tolerancia, iteraciones):

    f_evaluada = f.evalf(subs={symbols('x'):semilla})

    if (abs(f_evaluada) <= tolerancia or iteraciones == 0):
        return semilla

    siguiente = g(semilla)
    return punto_fijo_rec(g,f, siguiente, tolerancia, iteraciones - 1)

def punto_fijo(f, intervalo, tolerancia, iteraciones=-1):

    g = obtener_g(f)

    if(existe_unico_p_fijo(g,symbols('x'),intervalo)):
        semilla = intervalo[0]
        raiz = punto_fijo_rec(lambdify(symbols('x'),g), sympify(f), semilla, tolerancia, iteraciones)
        return raiz

    else:
        return "No es posible aplicar punto fijo dada la falta de existencia y/o unicidad del punto fijo"

if __name__ == "__main__":

    print("la raiz hallada con p fijo es: " +  str(print(punto_fijo("4.25 * pi * x ** 2 - (pi * x ** 3) / 3 - 180.52", (4,5), 1e-5, 30))))