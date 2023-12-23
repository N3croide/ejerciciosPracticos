import os
borrarPantalla = lambda : os.system('cls')
pausa = lambda : os.system('pause')

menuPrincipal = """
1. Registrar Dependencia
2. Registrar consumo por dependencia : Tengan en cuenta que se debe registrar los valores
consumidos por los dispositivos en cada una de las oficinas.
3. Ver CO2 producido
4. Dependencia que produce mayor CO2
5. Salir

"""

menuConsumo = """
1. Registrar consumo de dispositivos
2. Registrar consumo de transporte
3. Registrar consumo de electricidad
4. Volver atras"""


def mostrarMenu() -> int:
    while(True):
        try:
            print(menuPrincipal)
            optMenu = int(input("Seleccione una opcion: "))
        except ValueError:
            print("Ingrese un valor valido.")
            pausa()
        else:
            if (optMenu in [1,2,3,4,5]):
                return optMenu
            else:
                borrarPantalla()
                print("Ingrese un numero del 1 al 5.")
                pausa()

def mostrarMenuConsumo() -> int:
    while(True):
        try:
            print(menuConsumo)
            optMenu = int(input("Seleccione una opcion: "))
        except ValueError:
            print("Ingrese un valor valido.")
            pausa()
        else:
            if (optMenu in [1,2,3,4]):
                return optMenu
            else:
                borrarPantalla()
                print("Ingrese un numero del 1 al 4.")
                pausa()
