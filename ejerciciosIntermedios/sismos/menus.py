import os

menuP = """1. Registrar Ciudad
2. Registrar Sismo
3. Buscar sismos por ciudad
4. Informe de riesgo
5. Salir

"""
borrarPantalla = lambda : os.system("cls")
pausa = lambda : input("Presione cualquier tecla para continuar...")

def menuPrincipal() -> int:
    while(True):
        print(menuP)
        try:
            optMenu = int(input("Seleccione una opcion: "))
        except ValueError:
            borrarPantalla()
            print("Ingrese un numero valido.")
            pausa()
        else:
            if(optMenu in [1,2,3,4,5]):
                return optMenu
            else:
                borrarPantalla()
                print("Ingrese una opcion valida")
                pausa()

