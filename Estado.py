from Pais import Pais

class Estado(Pais):
    codigoEstado = 0
    nombreEstado = ""
    descripcion = ""

    def verDatos(self):
        print("===Datos de estado===")
        print("Codigo estado: ", self.codigoEstado)
        print("Nombre estado: ", self.nombreEstado)
        print("Descripcion: ", self.descripcion)
        super().verDatos()
