import TP1.MetodosBusquedaRaices.CalculadoraRaices as CR
import tabulate as tab

PRECISION_CALC_32_BIT = 1e-7

if __name__ == "__main__":

    coeficientes_polinomios = ["a=6 b=4 c=12",
                               "a=1 b=0 c=0",
                               "a=1 b=0 c=-1",
                               "a=1 b=1e20 c=1e5",
                               "a=1 b=1e-56 c=-10",
                               "a=1e-3 b=1 c=1e-5"]

    raices_convencionales = []
    raices_correctas = []
    # Realizo pruebas con metodo convencional

    raices_convencionales.append(str(CR.resolvente_convencional(6, 4, 12)))

    # Ejemplo con una raiz real doble (coeficientes a = 1, b = 0, c = 0)
    raices_convencionales.append(CR.resolvente_convencional(1, 0, 0))

    #  Ejemplo con dos raices reales (coeficientes a = 1, b = 0, c = -1)
    raices_convencionales.append(CR.resolvente_convencional(1, 0, -1))

    # Ejemplo con coeficientes dispares (coeficientes a = 1, b = 1e20, c = 1e5
    raices_convencionales.append(CR.resolvente_convencional(1, 1e20, 1e5))

    # Ejemplo con coeficientes dispares (coeficientes a = 1e-56, b = 1e10, c = -10)
    raices_convencionales.append(CR.resolvente_convencional(1, 1e-56, -10))

    # Ejemplo con coeficientes dispares (coeficientes a = 1e-3, b = 1, c = 1e-5)
    raices_convencionales.append(CR.resolvente_convencional(1e-3, 1, 1e-5))

    #==============================================================================================================
    # Realizo pruebas con metodo Correcto

    # Ejemplo sin raices reales coeficientes a = 6, b = 4, c = 12
    raices_correctas.append(str(CR.calcular_raices(6, 4, 12, PRECISION_CALC_32_BIT)))

    # Ejemplo con una raiz real doble (coeficientes a = 1, b = 0, c = 0)
    raices_correctas.append(CR.calcular_raices(1, 0, 0, PRECISION_CALC_32_BIT))

    # Ejemplo con dos raices reales (coeficientes a = 1, b = 0, c = -1)
    raices_correctas.append(CR.calcular_raices(1, 0, -1, PRECISION_CALC_32_BIT))

    #Ejemplo con coeficientes dispares (coeficientes a = 1, b = 1e20, c = 1e5)
    raices_correctas.append(CR.calcular_raices(1, 1e20, 1e5, PRECISION_CALC_32_BIT))

    #Ejemplo con coeficientes dispares (coeficientes a = 1e-56, b = 1e10, c = -10)
    raices_correctas.append(CR.calcular_raices(1, 1e-56, -10, PRECISION_CALC_32_BIT))

    # Ejemplo con coeficientes dispares (coeficientes a = 1e-3, b = 1, c = 1e-5)
    raices_correctas.append(CR.calcular_raices(1e-3, 1, 1e-5, PRECISION_CALC_32_BIT))

    tablita = zip(coeficientes_polinomios, raices_convencionales, raices_correctas)
    encabezados = ['Coeficientes de polinomio', 'Resultado Metodo convencional', 'Resultado Metodo Correcto']
    print(tab.tabulate(tablita, headers=encabezados, floatfmt=".8f"))








