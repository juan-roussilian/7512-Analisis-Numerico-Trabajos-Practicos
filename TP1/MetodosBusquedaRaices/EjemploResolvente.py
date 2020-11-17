from TP1.MetodosBusquedaRaices.CalculadoraRaices import calcular_raices

if __name__ == "__main__":

    # Ejemplo sin raices reales
    print("\nLas raices son", calcular_raices(6, 4, 12))

    # Ejemplo con una raiz real doble
    print("\nLas raices son", calcular_raices(1, 0, 0))

    # Ejemplo con dos raices reales
    print("\nLas raices son", calcular_raices(1, 0, -1))

    # Ejemplo que rompa por punto flotante

    print("\nLas raices son", calcular_raices(1, 1e5, 1e-2))
    # print("\nLas raices son", calculadora.calcular_raices_polinomio_segundo_orden(1e-56,1e20,-1))
