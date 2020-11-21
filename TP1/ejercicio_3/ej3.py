from scipy.optimize import brentq

from TP1.MetodosBusquedaRaices.Biseccion import biseccion
from TP1.MetodosBusquedaRaices.CalculadoraRaices import *
from TP1.MetodosBusquedaRaices.EstimacionConvergencia import estimar_orden_convergencia
from TP1.MetodosBusquedaRaices.EstimacionConvergencia import estimar_orden_convergencia, estimar_constante_asintontica
from TP1.MetodosBusquedaRaices.NewtonRaphson import newton_raphson
from TP1.MetodosBusquedaRaices.NewtonRaphsonModificado import newton_raphson_mod
from TP1.MetodosBusquedaRaices.PuntoFijo import punto_fijo
from TP1.MetodosBusquedaRaices.RepresentacionHistorias import graficar, tabular_historia_precision5, \
    tabular_historia_precision13
from TP1.MetodosBusquedaRaices.Secante import secante

RADIO = 4.25


def f1(x):
    return 4.25 * math.pi * x ** 2 - (math.pi * x ** 3) / 3 - 180.52


def f1_prima(x):
    return 2 * math.pi * RADIO * x - math.pi * x ** 2

def calcular_convergencia_promedio(convergencias):
    aux_convergencias = [x[1] for x in convergencias]
    return  sum(aux_convergencias)/len(aux_convergencias)



def ej_3_raices():  # comentamos los graficos de convergencia pues no pudimos debuggear
    historias_tol_5 = {}
    historias_tol_13 = {}
    convergencias_5 = {}
    convergencias_13 = {}
    constantes_lambda_5 = {}
    constantes_lambda_13 = {}

    ################################### Tolerancia 1e-5########################################################
    #BIS
    raiz, historia_bis_5, it_bis_5 = biseccion(f1, (0, 2 * RADIO), 1e-5)
    tabular_historia_precision5(historia_bis_5, "Biseccion 1e-5", it_bis_5)
    historias_tol_5["BIS5"] = historia_bis_5
    convergencias_5["BIS5"] = estimar_orden_convergencia(historia_bis_5, it_bis_5)
    convergencia_prom_bis_5 = calcular_convergencia_promedio(convergencias_5["BIS5"])
    constantes_lambda_5["BIS5"] = estimar_constante_asintontica(historia_bis_5, convergencia_prom_bis_5)

    #PF
    raiz, historia_pf_5, it_pf_5 = punto_fijo("4.25 * pi * x ** 2 - (pi * x ** 3) / 3 - 180.52", (RADIO, 6), 1e-5)
    tabular_historia_precision5(historia_pf_5, "Punto Fijo", it_pf_5)
    historias_tol_5["PF5"] = historia_pf_5
    convergencias_5["PF5"] = estimar_orden_convergencia(historia_pf_5, it_pf_5)
    convergencia_prom_pf_5 = calcular_convergencia_promedio(convergencias_5["PF5"])
    constantes_lambda_5["PF5"] = estimar_constante_asintontica(historia_pf_5, convergencia_prom_pf_5)

    #NR
    raiz, historia_nr_5, it_nr_5 = newton_raphson(f1, (RADIO, 2 * RADIO), 1e-5)
    tabular_historia_precision5(historia_nr_5, "Newton-Raphson", it_nr_5)
    historias_tol_5["NR5"] = historia_nr_5
    '''
    NR con tol 1e-5 no tiene suficientes iteraciones como para calcular convergencia
    convergencias_5["NR5"] = estimar_orden_convergencia(historia_nr_5, it_nr_5)
    convergencia_prom_nr_5 = calcular_convergencia_promedio(convergencias_5["NR5"])
    constantes_lambda_5["NR5"] = estimar_constante_asintontica(historia_nr_5,convergencia_prom_nr_5)
    '''

    #SEC
    raiz, historia_sec_5, it_sec_5 = secante(f1, (RADIO, 2 * RADIO), 1e-5)
    tabular_historia_precision5(historia_sec_5, "Secante", it_sec_5)
    historias_tol_5["SEC5"] = historia_sec_5
    convergencias_5["SEC5"] = estimar_orden_convergencia(historia_sec_5,it_sec_5)
    convergencia_prom_sec_5 = calcular_convergencia_promedio(convergencias_5["SEC5"])
    constantes_lambda_5["SEC5"] = estimar_constante_asintontica(historias_tol_5["SEC5"],convergencia_prom_sec_5)

    #NR-M
    raiz, historia_nrm_5, it_nrm_5 = newton_raphson_mod(f1, (RADIO, 2 * RADIO), 1e-5)
    tabular_historia_precision5(historia_nrm_5, "Newton-Raphson-MOD", it_nrm_5)
    historias_tol_5["NRM5"] = historia_nrm_5
    convergencias_5["NRM5"] = estimar_orden_convergencia(historia_nrm_5,it_nrm_5)
    convergencia_prom_nrm_5 = calcular_convergencia_promedio(convergencias_5["NRM5"])
    constantes_lambda_5["NRM5"] = estimar_constante_asintontica(historias_tol_5["NRM5"], convergencia_prom_nrm_5)


    ################################### Tolerancia 1e-13########################################################
    #BIS
    raiz, historia_bis_13, it_bis_13 = biseccion(f1, (0, 2 * RADIO), 1e-13)
    tabular_historia_precision13(historia_bis_13, "Biseccion 1e-13", it_bis_13)
    historias_tol_13["BIS13"] = historia_bis_13
    convergencias_13["BIS13"] = estimar_orden_convergencia(historia_bis_13, it_bis_13)
    convergencia_prom_bis_13 = calcular_convergencia_promedio(convergencias_13["BIS13"])
    constantes_lambda_13["BIS13"] = estimar_constante_asintontica(historias_tol_13["BIS13"],convergencia_prom_bis_13)
    #PF
    raiz, historia_pf_13, it_pf_13 = punto_fijo("4.25 * pi * x ** 2 - (pi * x ** 3) / 3 - 180.52", (RADIO, 6), 1e-13)
    tabular_historia_precision13(historia_pf_13, "Punto Fijo", it_pf_13)
    historias_tol_13["PF13"] = historia_pf_13
    convergencias_13["PF13"] = estimar_orden_convergencia(historia_pf_13, it_pf_13)
    convergencia_prom_pf_13 = calcular_convergencia_promedio(convergencias_13["PF13"])
    constantes_lambda_13["PF13"] = estimar_constante_asintontica(historias_tol_13["PF13"], convergencia_prom_pf_13)
    #NR
    raiz, historia_nr_13, it_nr_13 = newton_raphson(f1, (RADIO, 2 * RADIO), 1e-13)
    tabular_historia_precision13(historia_nr_13, "Newton-Raphson", it_nr_13)
    historias_tol_13["NR13"] = historia_nr_13
    convergencias_13["NR13"] = estimar_orden_convergencia(historia_nr_13, it_nr_13)
    convergencia_prom_nr_13 = calcular_convergencia_promedio(convergencias_13["NR13"])
    constantes_lambda_13["NR13"] = estimar_constante_asintontica(historias_tol_13["NR13"], convergencia_prom_nr_13)
    # SEC
    raiz, historia_sec_13, it_sec_13 = secante(f1, (RADIO, 2 * RADIO), 1e-13)
    tabular_historia_precision13(historia_sec_13, "Secante", it_sec_13)
    historias_tol_13["SEC13"] = historia_sec_13
    convergencias_13["SEC13"] = estimar_orden_convergencia(historia_sec_13, it_sec_13)
    convergencia_prom_sec_13 = calcular_convergencia_promedio(convergencias_13["SEC13"])
    constantes_lambda_13["SEC13"] = estimar_constante_asintontica(historias_tol_13["SEC13"], convergencia_prom_sec_13)
    #NR-M
    raiz, historia_nrm_13, it_nrm_13 = newton_raphson_mod(f1, (RADIO, 2 * RADIO), 1e-13)
    tabular_historia_precision13(historia_nrm_13, "Newton-Raphson-MOD", it_nrm_13)
    historias_tol_13["NRM13"] = historia_nrm_13
    convergencias_13["NRM13"] = estimar_orden_convergencia(historia_nrm_13, it_nrm_13)
    convergencia_prom_nrm_13 = calcular_convergencia_promedio(convergencias_13["NRM13"])
    constantes_lambda_13["NRM13"] = estimar_constante_asintontica(historias_tol_13["NRM13"], convergencia_prom_nrm_13)
    ##################################################################################################################


    graficar(historias_tol_5, "Comparación metodos busqueda raices con tolerancia 1e-5","Raiz estimada",escala_y="log")
    graficar(historias_tol_13,"Comparación metodos busqueda raices con tolerancia 1e-13","Raiz estimada",escala_y="log")
    graficar(convergencias_5, "Comparación convergencias metodos 1e-5","Orden convergencia")
    graficar(convergencias_13, "Comparación convergencias metodos 1e-13", "Orden convergencia")
    graficar(constantes_lambda_5, "Constantes asintoticas con tolerancia 1e-5", "Lambda")
    graficar(constantes_lambda_13,"Constantes asintoticas con tolerancia 1e-13","Lambda")


    print("Hallando raices de f1 por metodo brentq incluido en scipy.optimize")
    print(brentq(f1, 0, 2 * RADIO))

def raices_derivada():
    print("La raices de la derivada calculada con la calculadora del punto 2" + str(
        calcular_raices(math.pi, 2 * math.pi * RADIO, 0, 1e-7)))

if __name__ == "__main__":
    ej_3_raices()
    raices_derivada()
