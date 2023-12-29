import os, menus as me, campers as camp, rutas as rut, otrasfunciones as otf,pruebas as pb

db = {
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
while(True):
    opt = me.seleccionMenu([1,2,3,4,5,6,7,8,9],1)
    if(opt == 1):
        camp.registrarCamper(campersNuevos)
    elif(opt == 2):
        pb.pruebasInicicales(campersNuevos)
    elif(opt == 3):
        rut.registrarRuta(db)
    elif(opt == 4):
        rut.regTrainers(trainers, db)
    elif(opt == 5):#matriculas
        camp.matriculaCamers(db, campersNuevos, salones)
    elif(opt == 6):#pruebas
        pb.pruebasModulos(db)
    elif(opt == 7):#reportes
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
            camp.mostrarCampers("bajo rendimiento",db.get("NodeJS").get("campers"))
            print("\nCampers con bajo rendimiento en la ruta Java\n")
            camp.mostrarCampers("bajo rendimiento",db.get("Java").get("campers"))
            print("\nCampers con bajo rendimiento en la ruta NetCore\n")
            camp.mostrarCampers("bajo rendimiento",db.get("NetCore").get("campers"))
        elif optRep == 5:
            otf.borrarPantalla()
            for key in db.keys():
                print(f"Ruta de {key}\nEntrenador asignado: {db.get(key).get('trainer')}")
                camp.mostrarCampers("",db.get(key).get("campers"))
        elif optRep == 6:
            otf.borrarPantalla()
            for key in db.keys():
                print(f"Ruta de {key}\nEntrenador asignado: {db.get(key).get('trainer')}")
                if not db.get(key).get('modulos'):
                    print("No se encuentra modulo registrado.")
                    pass
                for key, item in db.get(key).get("modulos").items():
                    print(f"Modulo: {key:<20} Estudiantes Aprobados: {item.get('resultados').get('aprobados'):<5} Estudiantes Aprobados: {item.get('resultados').get('reprobados'):<5}")
                otf.pausa()     
        elif optRep == 7:
            pass
    elif(opt == 9):
        otf.borrarPantalla()
        print("Gracias por utilizar nuestro software.")
        otf.pausa()
        break