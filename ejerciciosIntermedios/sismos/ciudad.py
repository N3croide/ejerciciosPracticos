import sismos as sism, os
borrarPantalla = lambda : os.system("cls")
pausa = lambda : input("Presione cualquier tecla para continuar...")

def registrarCiudad() -> list:
    while(True):
        nombreCiudad = input("Ingrese el nombre de la ciudad: ")
        if (nombreCiudad != ""):
            ciudad = [nombreCiudad,[]]
            return ciudad
        else:
            print("El campo no puede estar vacio")
            pausa()
            
def sismosPorCiudad(ciudades : list):
    nombreCiudad = input("Ingrese el nombre de la ciudad: ")
    for item in ciudades:
        if item[0] == nombreCiudad:
            sism.buscarSismo(item)
        else:
            print("El nombre de la ciudad no existe.")