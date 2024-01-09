import os, menus as me, campers as camp, rutas as rut, otrasfunciones as otf,pruebas as pb, coreFileManager as cfm

db = {}
rutas = {
    "NodeJS" : {
        "modulos":{},
        "campers":{},
        "trainer":""
    },
    "Java" : {
        "modulos":{},
        "campers":{},
        "trainer":""
    },
    "NetCore" : {
        "modulos":{},
        "campers":{},
        "trainer":""
    }

}
campersNuevos = {}
trainers = []
salones = {1: {"nombre":"Sputnik","campers": 0}, 2: {"nombre": "Apolo", "campers": 0}, 3: {"nombre": "Artemis", "campers": 0}}
otf.borrarPantalla()
db.update({'rutas':rutas,'campersNuevos': campersNuevos, 'trainers':trainers , 'salones':salones})
cfm.checkFile(db)
rutas, campersNuevos, trainers, salones = cfm.loadFile(rutas, campersNuevos, trainers, salones)
while(True):
    opt = me.seleccionMenu([1,2,3,4,5,6,7,8,9],1)
    if(opt == 1):
        camp.registrarCamper(campersNuevos)
        cfm.updateFile('campersNuevos',campersNuevos)
    elif(opt == 2):
        pb.pruebasInicicales(campersNuevos)
        cfm.updateFile('campersNuevos',campersNuevos)
    elif(opt == 3):
        rut.registrarRuta(rutas)
        cfm.updateFile('rutas',rutas)
    elif(opt == 4):
        rut.regTrainers(trainers, rutas)
        cfm.updateFile('rutas',rutas)
        cfm.updateFile('trainers',trainers)
    elif(opt == 5):
        camp.matriculaCamers(rutas, campersNuevos, salones)
        cfm.updateFile('rutas',rutas)
        cfm.updateFile('salones',salones)
        cfm.updateFile('campersNuevos', campersNuevos)
    elif(opt == 6):
        pb.pruebasModulos(rutas)
        cfm.updateFile('rutas',rutas)
    elif(opt == 7):
        optRep = me.seleccionMenu([1,2,3,4,5,6,7],3)
        if optRep == 1:
            camp.mostrarCampers("inscrito",campersNuevos)
        elif optRep == 2:
            camp.mostrarCampers("aprobado",campersNuevos)
        elif optRep == 3:
            otf.borrarPantalla()
            print("Los entrenadores que se encuentran trabajando en campus son los sig: ")
            print(trainers)
            otf.pausa()
        elif optRep == 4:
            otf.borrarPantalla()
            print("\nCampers con bajo rendimiento en la ruta NodeJS\n")
            camp.mostrarCampers("bajo rendimiento",rutas.get("NodeJS").get("campers"))
            print("\nCampers con bajo rendimiento en la ruta Java\n")
            camp.mostrarCampers("bajo rendimiento",rutas.get("Java").get("campers"))
            print("\nCampers con bajo rendimiento en la ruta NetCore\n")
            camp.mostrarCampers("bajo rendimiento",rutas.get("NetCore").get("campers"))
        elif optRep == 5:
            for key in rutas.keys():
                otf.borrarPantalla()
                print(f"Ruta de {key}\nEntrenador asignado: {rutas.get(key).get('trainer')}")
                camp.mostrarCampers("",rutas.get(key).get("campers"))
        elif optRep == 6:
            otf.borrarPantalla()
            for key in rutas.keys():
                otf.borrarPantalla()
                print(f"Ruta de {key}\nEntrenador asignado: {rutas.get(key).get('trainer')}")
                if not rutas.get(key).get('modulos'):
                    print("No se encuentra modulo registrado.")
                    otf.pausa()
                    pass
                for key, item in rutas.get(key).get("modulos").items():
                    print(f"Modulo: {key:<20} Estudiantes Aprobados: {item.get('resultados').get('aprobados'):<5} Estudiantes Aprobados: {item.get('resultados').get('reprobados'):<5}")
                otf.pausa()     
        elif optRep == 7:
            pass
    elif(opt == 9):
        otf.borrarPantalla()
        print("Gracias por utilizar nuestro software.")
        otf.pausa()
        break