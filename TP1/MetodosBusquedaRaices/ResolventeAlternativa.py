import math

class ResolventeAlternativa:

    def __init__(self, primer_coef, segundo_coef, tercer_coef):
        self.coef_segundo_grado = primer_coef
        self.coef_primer_grado = segundo_coef
        self.termino_independiente = tercer_coef

    def obtener_raices(self):
        return self.__aplicar_Bhaskara()

    def __aplicar_Bhaskara(self):
        discriminante = math.pow(self.coef_primer_grado, 2) - (4 * self.coef_segundo_grado * self.termino_independiente)

        if discriminante >= 0:
            primer_raiz =  -2 * self.termino_independiente / (self.coef_primer_grado + math.sqrt(discriminante))
            segunda_raiz =  -2 * self.termino_independiente / (self.coef_primer_grado - math.sqrt(discriminante))

            if primer_raiz == segunda_raiz:
                return primer_raiz
            else:
                return primer_raiz, segunda_raiz

        else:
            return None
