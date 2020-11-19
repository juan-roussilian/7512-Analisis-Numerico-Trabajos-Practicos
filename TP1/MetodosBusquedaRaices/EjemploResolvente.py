from TP1.MetodosBusquedaRaices.CalculadoraRaices import calcular_raices

PRECISION_CALC_32_BIT = 1e-7

if __name__ == "__main__":

    # Ejemplo sin raices reales
    print("\nLas raices son", calcular_raices(6, 4, 12, PRECISION_CALC_32_BIT))

    # Ejemplo con una raiz real doble
    print("\nLas raices son", calcular_raices(1, 0, 0,  PRECISION_CALC_32_BIT))

    # Ejemplo con dos raices reales
    print("\nLas raices son", calcular_raices(1, 0, -1, PRECISION_CALC_32_BIT))

    # Ejemplo que rompa por punto flotante

    print("\nLas raices son", calcular_raices(1, 1e20, 1e5, PRECISION_CALC_32_BIT))
    # print("\nLas raices son", calculadora.calcular_raices_polinomio_segundo_orden(1e-56,1e20,-1))
