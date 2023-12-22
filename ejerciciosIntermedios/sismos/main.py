import menus as me, os, ciudad as cid, sismos as sism
borrarPantalla = lambda : os.system("cls")
pausa = lambda : input("Presione cualquier tecla para continuar...")

optMenu = 0
ciudades = []
while(True):
    borrarPantalla()
    optMenu = me.menuPrincipal()
    if(optMenu == 1):
        if(len(ciudades) < 5):
            ciudades.append(cid.registrarCiudad())
        else:
            print("ERROR :  El maximo de ciudades registradas es cinco(5).")
        print("Las ciudades registradas son: ",ciudades)
        pausa()
    elif(optMenu == 2):

        noExiste = True
        nombreCiudad = input("Ingrese el nombre de la ciudad: ")

        for index, ciudadRegistrada in enumerate(ciudades):
            if(nombreCiudad == ciudadRegistrada[0]):
                sism.registrarSismo(ciudades[index])
                noExiste = False

        if(noExiste):
            print("El nombre de la ciudad no esta registrado.")
            pausa()
            
    elif(optMenu == 3):
        cid.sismosPorCiudad(ciudades)
    elif(optMenu == 4):
        sism.informeSismos(ciudades)
    elif(optMenu == 5):
        break 
