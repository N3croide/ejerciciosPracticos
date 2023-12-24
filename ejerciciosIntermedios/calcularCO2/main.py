import os, menus as me, dependencias as dp, c02 as c
borrarPantalla = lambda : os.system('cls')
pausa = lambda : os.system('pause')

dependencias = {}
while(True):
    borrarPantalla()
    optMenu = me.mostrarMenu()
    if(optMenu == 1):
        dp.registrarDependencia(dependencias)
        pausa()
    elif(optMenu == 2):
        c.registrarConsumo(dependencias)
    elif(optMenu == 3):
        c.mostrarCO2(dependencias)
    elif(optMenu == 4):
        c.mayorCO2(dependencias)
    elif(optMenu == 5):
        print("Gracias por utilizar nuestro software")
        break