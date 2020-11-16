from ResolventeAlternativa import  ResolventeAlternativa
from ResolventeConvencional import  ResolventeConvencional

class CalculadoraRaices:

    def calcular_raices_polinomio_segundo_orden(self, primer_coef, segundo_coef, tercer_coef):

        # b >> a.c
        if (segundo_coef > primer_coef * segundo_coef) or (primer_coef == 0):
            formulaCorrecta = ResolventeAlternativa(primer_coef, segundo_coef, tercer_coef)
            return formulaCorrecta.obtener_raices()
        else:
            formulaCorrecta = ResolventeConvencional(primer_coef, segundo_coef, tercer_coef)
            return formulaCorrecta.obtener_raices()