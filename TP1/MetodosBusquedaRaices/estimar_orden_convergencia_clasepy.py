def estimarOrdenCovergencia(historiaRaices, nIteraciones):
    # 'nIteraciones' no cuenta el candidato inicial, por eso restamos  1
    alfa = np.zeros((nIteraciones-1,2)


    # Necesito 4 puntos; 1 para adelante, 2 para atras, n el actual, con lo
    # cual arranco en la posicion 3, o sea, indice 2
    # Recordar que 'nIteraciones' no tiene en cuenta el punto inicial de estimacion,
    # con lo cual no hace falta tener en cuenta el indice 0, y se suma 1 inlcuida
    # la ultima estimacion.

    for n in range (3-1, nIteraciones - 1):
        e_n_mas_1 = historiaRaices[n+1][1] - historiaRaices[n][1]
        e_n = historiaRaices[n][1] - historiaRaices[n-1][1]
        e_n_menos_1 = historiaRaices[n-1][1] - historiaRaices[n-2][1]

        #falta chequar que nos e divida por cero.
        alfa[n] =  n, np.log10(np.abs(e_n_mas_1/e_n))/ np.log10(np.abs(e_n/e_n_menos_1))

    return alfa.
