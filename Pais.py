from Continente import Continente

class Pais(Continente):
    codigoPais = 0
    nombrePais = ""

    def verDatos(self):
        print("===Datos de pais===")
        print("Codigo Pais: ", self.codigoPais)
        print("Nombre Pais: ", self.nombrePais)
        super().verDatos()