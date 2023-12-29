import otrasfunciones as otf, menus as me


def registrarRuta(rutas : dict):
    opcionesBases = {
    (1, 2): "Principal: Mysql -- Alternativa: MongoDb",
    (1, 3): "Principal: Mysql -- Alternativa: Postgresql",
    (2, 1): "Principal: MongoDb -- Alternativa: Mysql",
    (2, 3): "Principal: MongoDb -- Alternativa: Postgresql",
    (3, 1): "Principal: Postgresql -- Alternativa: Mysql",
    (3, 2): "Principal: Postgresql -- Alternativa: MongoDb"
}
    optRuta = me.seleccionMenu([1,2,3,4], 2)
    rutaModulo = {"FundamentosProgramacion":{"contenido":"(Introducción a la algoritmia, PSeInt y Python)", "resultados":{"aprobados":0,"reprobados":0}},
            "ProgramacionWeb": {"contenido":"(HTML, CSS y Bootstrap)","resultados":{"aprobados":0,"reprobados":0}},
            "ProgramacionFormal":{"contenido":"(Java, JavaScript, C#)","resultados":{"aprobados":0,"reprobados":0}} ,
            "BasesDatos": {"contenido":"","resultados":{"aprobados":0,"reprobados":0}},
            "BackEnd": {"contenido":"(NetCore, Spring Boot, NodeJS y Express)","resultados":{"aprobados":0,"reprobados":0}}}
    nombreRuta = ""
    if (optRuta == 1):
        nombreRuta = "NodeJS"
    elif (optRuta == 2):
        nombreRuta = "Java"
    elif (optRuta == 3):
        nombreRuta = "NetCore"    
    elif (optRuta == 4):
        return
    otf.borrarPantalla()
    print("Seleccione una base de datos principal y una alternativa")
    otf.pausa()
    optDbP = me.seleccionMenu([1,2,3],4)
    optDbS = me.seleccionMenu([1,2,3],4)
    if (optDbP, optDbS) in opcionesBases:
      rutaModulo.get("BasesDatos").update({"contenido": opcionesBases[(optDbP, optDbS)]})
    
    rutas.get(nombreRuta).update({"modulos": rutaModulo})
    otf.borrarPantalla()
    print('\n'.join(f'{key}: {value}' for key,value in rutas.get(nombreRuta).get('modulos').items()))
    otf.pausa()

def regTrainers(trainers : tuple, db :dict):
    otf.borrarPantalla()
    nombre = otf.comprobarDato("Ingrese el nombre del trainer: ", str)
    trainers.append(nombre)
    print("A continuacion selecccione la ruta a la que sera asignado el trainer")
    otf.pausa()
    optRuta = me.seleccionMenu([1,2,3,4],2)
    nombreRuta = ""
    if (optRuta == 1):
        nombreRuta = "NodeJS"
    elif (optRuta == 2):
        nombreRuta = "Java"
    elif (optRuta == 3):
        nombreRuta = "NetCore"    
    elif (optRuta == 4):
        return
    db.get(nombreRuta).update({"trainer": nombre})
    print(nombre, "asignado a ",nombreRuta)
    otf.pausa()