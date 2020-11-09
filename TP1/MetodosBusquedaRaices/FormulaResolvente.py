import math

class FormulaResolvente:

    def __init__(self, primerCoeficiente, segundoCoeficiente, tercerCoeficiente):
        self.coeficiente1erGrado = primerCoeficiente
        self.coeficiente2doGrado = segundoCoeficiente
        self.coeficiente3erGrado = tercerCoeficiente

    def obtenerRaices(self):
        return self.__aplicarBhaskara()

    def __aplicarBhaskara(self):
        discriminante = math.pow(self.coeficiente2doGrado, 2) - (4 * self.coeficiente1erGrado * self.coeficiente3erGrado)

        if discriminante >= 0:
            primerRaiz = (-self.coeficiente2doGrado) + (math.sqrt(discriminante)/2 * self.coeficiente1erGrado)
            segundaRaiz = (-self.coeficiente2doGrado) - (math.sqrt(discriminante)/2 * self.coeficiente1erGrado)

            if primerRaiz == segundaRaiz:
                return primerRaiz
            else:
                return primerRaiz, segundaRaiz

        else:
            return None
