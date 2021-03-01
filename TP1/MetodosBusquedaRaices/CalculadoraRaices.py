import math
import numpy as np

DIF_EXPONENTES_1 = 6
DIF_EXPONENTES_2 = 10

# def resolvente_alternativa(coef_a, coef_b, coef_c):
#    discriminante = math.pow(coef_b, 2) - (4 * coef_a * coef_c)
#
#    if discriminante >= 0:
#
#        primer_raiz = - 2 * coef_c / (coef_b + math.sqrt(math.pow(coef_b, 2) - (4 * coef_a * coef_c)))
#        segunda_raiz = - 2 * coef_c / (coef_b - math.sqrt(math.pow(coef_b, 2) - (4 * coef_a * coef_c)))
#
#        return primer_raiz, segunda_raiz
#    else:
#        return None


def resolvente_convencional(coef_a, coef_b, coef_c):
    discriminante = math.pow(coef_b, 2) - (4 * coef_a * coef_c)

    if discriminante >= 0:

        primer_raiz = (-coef_b + math.sqrt(discriminante)) / (2 * coef_a)
        segunda_raiz = (-coef_b - math.sqrt(discriminante)) / (2 * coef_a)

        return primer_raiz, segunda_raiz

    else:
        return None


def resolvente_vieta(coef_a, coef_b, coef_c):
    return -coef_b / coef_a, -coef_c / coef_b


def exponentes_dispares(coef_a, coef_b, coef_c):
    return (np.log10(abs(coef_b)) - np.log10(abs(coef_a * coef_c))) > DIF_EXPONENTES_1


def calcular_raices(coef_a, coef_b, coef_c, tolerancia):
    if abs(coef_b) < tolerancia:

        # p = c -> el polinomio es una constante
        if abs(coef_a) < tolerancia:
            return None

        # p = a * a^2 -> 0 raiz doble
        elif abs(coef_c) < tolerancia:
            return 0, 0

    elif abs(coef_a) < tolerancia:

        # p = bx -> 0 raiz simple
        if abs(coef_c) < tolerancia:
            return 0, None

        # p = bx + c -> recta, raiz simple
        return -coef_c / coef_b

        # nada se anula, y b^2 > |ac|
    if abs(coef_c) > tolerancia and exponentes_dispares(coef_a, coef_b, coef_c):
        return resolvente_vieta(coef_a, coef_b, coef_c)

    return resolvente_convencional(coef_a, coef_b, coef_c)
