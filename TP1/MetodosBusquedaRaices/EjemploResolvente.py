from CalculadoraRaices import CalculadoraRaices

if __name__ == "__main__":
    calculadora = CalculadoraRaices()

    #Ejemplo sin raices reales
    #resolvente = ResolventeConvencional(6, 4, 12)
    print("\nLas raices son", calculadora.calcular_raices_polinomio_segundo_orden(6,4,12))
    #Ejemplo con una raiz real doble
    #resolvente = ResolventeConvencional(1, 0, 0)
    print("\nLas raices son", calculadora.calcular_raices_polinomio_segundo_orden(1,0,0))

    # Ejemplo con dos raices reales
    #resolvente = ResolventeConvencional(1, 0, -1)
    print("\nLas raices son", calculadora.calcular_raices_polinomio_segundo_orden(1,0,-1))

    # Ejemplo que rompa por punto flotante
    #resolvente = ResolventeConvencional(1e-56, 1e20, -1)
    print("\nLas raices son", calculadora.calcular_raices_polinomio_segundo_orden(1e-56,1e20,-1))


