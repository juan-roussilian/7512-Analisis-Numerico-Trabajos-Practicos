import math
import numpy as np

def resolvente_convencional(coef_a, coef_b, coef_c):

    discriminante = math.pow(coef_b, 2) - (4 * coef_a * coef_c)

    if discriminante >= 0:

        primer_raiz = (-coef_b + math.sqrt(discriminante)) / (2 * coef_a)
        segunda_raiz = (-coef_b - math.sqrt(discriminante)) / (2 * coef_a)

        return primer_raiz, segunda_raiz

    else:
        return None


def resolvente_alternativa(coef_a, coef_b, coef_c):

    discriminante = math.pow(coef_b, 2) - (4 * coef_a * coef_c)

    if discriminante >= 0:

        primer_raiz = - 2 * coef_c / (coef_b + math.sqrt(math.pow(coef_b, 2) - (4 * coef_a * coef_c)))
        segunda_raiz = - 2 * coef_c / (coef_b - math.sqrt(math.pow(coef_b, 2) - (4 * coef_a * coef_c)))

        return  primer_raiz, segunda_raiz
    else:
        return None


def calcular_raices(coef_a, coef_b, coef_c):

    diferencia_exponentes = 6

    if(coef_a == 0 or coef_c == 0):
        if (np.log10(abs(coef_b)) - 0) > diferencia_exponentes :
            return resolvente_alternativa(coef_a, coef_b, coef_c)
        else:
            return resolvente_convencional(coef_a, coef_b, coef_c)

    if(coef_b == 0 ):
        if (0 - np.log10(abs(coef_a * coef_c))) > diferencia_exponentes:
            return resolvente_alternativa(coef_a, coef_b, coef_c)
        else:
            return resolvente_convencional(coef_a, coef_b, coef_c)

    else:
        if (np.log10(abs(coef_b)) - np.log10(abs(coef_a * coef_c))) > diferencia_exponentes:
            return resolvente_alternativa(coef_a, coef_b, coef_c)
        else:
            return resolvente_convencional(coef_a, coef_b, coef_c)