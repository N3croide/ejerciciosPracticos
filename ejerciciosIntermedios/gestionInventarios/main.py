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
        inv.actualizacionStock(productos)
    elif(optMenu == 4):
        inv.prodCriticos(productos)
    elif(optMenu == 5):
        inv.ganancia(productos)
    elif(optMenu == 6):
        borrarPantalla()
        print("Gracias por utilizar nuestro software.")
        pausa()
        break