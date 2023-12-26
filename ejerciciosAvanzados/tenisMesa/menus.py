import os

menuCategoria = """1. Novato
2. Intermedio
3. Avanzado
"""

menuPrincipal = """1. Registrar jugadores
2. Iniciar juego
3. Informe de jugador
4. Ganadores
5. Salir
"""
pausa = lambda : os.system('pause')
borrarPantalla = lambda : os.system('cls')

def seleccionMenu() -> int:
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

def seleccionCategoria() -> str:
    while(True):
        try:
            print(menuCategoria)
            optMenu = int(input("Seleccione una opcion: "))
        except ValueError:
            print("Ingrese un valor valido.")
            pausa()
        else:
            if (optMenu == 1):
                return "novato"
            elif (optMenu == 2):
                return "intermedio"
            elif (optMenu == 3):
                return "avanzado"
            else:
                borrarPantalla()
                print("Ingrese un numero del 1 al 3.")
                pausa()
