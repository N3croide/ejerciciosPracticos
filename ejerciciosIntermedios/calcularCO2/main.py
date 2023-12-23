import os, menus as me, dependencias as dp
borrarPantalla = lambda : os.system('cls')
pausa = lambda : os.system('pause')

dependencias = {}
while(True):
    borrarPantalla()
    optMenu = me.mostrarMenu()
    if(optMenu == 1):
        nuevaDependencia = dp.registrarDependencia()
        print(nuevaDependencia)
        dependencias.update(nuevaDependencia)
        pausa()
    elif(optMenu == 2):
        pass
    elif(optMenu == 3):
        pass
    elif(optMenu == 4):
        pass
    elif(optMenu == 5):
        print("Gracias por utilizar nuestro software")
        break