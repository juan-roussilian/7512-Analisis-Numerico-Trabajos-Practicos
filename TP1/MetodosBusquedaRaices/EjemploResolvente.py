from MetodosBusquedaRaices.ResolventeConvencional import ResolventeConvencional

if __name__ == "__main__":
    #Ejemplo sin raices reales
    resolvente = ResolventeConvencional(6, 4, 12)
    print("\nLas raices son",resolvente.obtener_raices())
    #Ejemplo con una raiz real doble
    resolvente = ResolventeConvencional(1, 0, 0)
    print("\nLas raices son", resolvente.obtener_raices())

    # Ejemplo con dos raices reales
    resolvente = ResolventeConvencional(1, 0, -1)
    print("\nLas raices son", resolvente.obtener_raices())

    # Ejemplo que rompa por punto flotante
    resolvente = ResolventeConvencional(1e-56, 1e20, -1)
    print("\nLas raices son", resolvente.obtener_raices())


