from Ciudad import Ciudad

ciudad = Ciudad()
print("====Ingrese los datos solicitados====")
ciudad.codigoCiudad = int(input("Ingrese el codigo de la ciudad: "))
ciudad.nombreCiudad = input("Ingrese el nombre de la ciudad: ")
ciudad.codigoEstado = int(input("Ingrese el codigo del estado: "))
ciudad.nombreEstado = input("Ingrese el nombre del estado: ")
ciudad.descripcion = input("Ingrese la descripcion del estado: ")
ciudad.codigoPais = int(input("Ingrese el codigo de pais: "))
ciudad.nombrePais = input("Ingrese el nombre del pais: ")
ciudad.codigoContinente = int(input("Ingrese el codigo del continente: "))
ciudad.nombreContinente = input("Ingrese el nombre del continente: ")

ciudad.verDatos()
