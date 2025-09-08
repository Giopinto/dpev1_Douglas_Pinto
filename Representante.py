from Empresa import Empresa

class Representante(Empresa):
    codigoRepresentante = 0
    nombreRepresentante = ""

    def verDatos(self):
        print("===Datos de representante===")
        print("Codigo representante: ", self.codigoRepresentante)
        print("Nombre representante: ", self.nombreRepresentante)
        super().verDatos()