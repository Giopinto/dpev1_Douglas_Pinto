from Estado import Estado

class Ciudad(Estado):
    codigoCiudad = 0
    nombreCiudad = ""

    def verDatos(self):
        print("===Datos de ciudad===")
        print("Codigo ciudad: ", self.codigoCiudad)
        print("Nombre ciudad: ", self.nombreCiudad)
        super().verDatos()