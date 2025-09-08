from Pais import Pais

class Empresa(Pais):
    codigoEmpresa = 0
    nombreEmpresa = ""
    telefonoEmpresa = 0

    def verDatos(self):
        print("===Datos de empresa===")
        print("Codigo empresa: ", self.codigoEmpresa)
        print("Nombre empresa: ", self.nombreEmpresa)
        print("Telefono Empresa: ", self.telefonoEmpresa)
        super().verDatos()
