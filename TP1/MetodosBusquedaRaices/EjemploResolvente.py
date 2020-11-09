from MetodosBusquedaRaices.FormulaResolvente import FormulaResolvente

if __name__ == "__main__":
    #Ejemplo sin raices reales
    resolvente = FormulaResolvente(6, 4, 12)
    print("\nLas raices son",resolvente.obtenerRaices())
    #Ejemplo con una raiz real doble
    resolvente = FormulaResolvente(1, 0, 0)
    print("\nLas raices son", resolvente.obtenerRaices())

    # Ejemplo con dos raices reales
    resolvente = FormulaResolvente(1, 0, -1)
    print("\nLas raices son", resolvente.obtenerRaices())

