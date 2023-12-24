import inventario  as inv, os

pausa = lambda : os.system('pause')
borrarPantalla = lambda : os.system('cls')

productos = {}

while(True):
    borrarPantalla()
    optMenu = inv.seleccionMenu()
    if(optMenu == 1 ):
        borrarPantalla()
        productos.update(inv.registrarProd(productos))
    elif(optMenu == 2):
        inv.verProd(productos)
        pausa()
    elif(optMenu == 3):
        pass
    elif(optMenu == 4):
        pass
    elif(optMenu == 5):
        pass
    elif(optMenu == 6):
        print("Gracias por utilizar nuestro software.")
        pausa()
        break