import os, menus as me, campers as camp, rutas as rut

rutas = {
    "NodeJS" : {
        "ruta":{"modulos":{},"resultados":{}},
        "estudiantes":{},
        "trainer":{}
    },
    "Java" : {
        "ruta":{"modulos":{},"resultados":{}},
        "estudiantes":{},
        "trainer":{}
    },
    "NetCore" : {
        "ruta":{"modulos":{},"resultados":{}},
        "estudiantes":{},
        "trainer":{}
    }

}
campersNuevos = {}
pausa = lambda : os.system('pause')
borrarPantalla = lambda : os.system('cls')


while(True):
    opt = me.seleccionMenu([1,2,3,4,5,6,7,8],1)
    if(opt == 1):
        campersNuevos.update(camp.registrarCamper())
    elif(opt == 2):
        pass
    elif(opt == 3):
        rut.registrarRuta(rutas)
    elif(opt == 4):
        pass
    elif(opt == 5):
        pass
    elif(opt == 6):
        pass
    elif(opt == 7):
        pass
    elif(opt == 8):
        borrarPantalla()
        print("Gracias por utilizar nuestro software.")
        pausa()
        break