import os, menus as me
pausa = lambda : os.system('pause')
borrarPantalla = lambda : os.system('cls')  
def comprobarDato (cadena, tipo):
    tipoUsuario = ''
    dato =''
    if(tipo == int):
        tipoUsuario = 'entero'
    elif(tipo == float):
        tipoUsuario = 'real'
    try:
        dato = tipo(input(f'{cadena}'))
    except ValueError:
        while(type(dato) != tipo):
            try:
                print(f'El dato debe ser de tipo {tipoUsuario}')
                dato = tipo(input(cadena))
            except ValueError:
                borrarPantalla()
        return dato
    else:
        return dato
 

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
    rutaModulo = {"FundamentosProgramacion": "(Introducción a la algoritmia, PSeInt y Python)",
            "ProgramacionWeb": "(HTML, CSS y Bootstrap)",
            "ProgramacionFormmal": "(Java, JavaScript, C#)",
            "BasesDatos": "",
            "BackEnd": "(NetCore, Spring Boot, NodeJS y Express)"}
    nombreRuta = ""
    if (optRuta == 1):
        nombreRuta = "NodeJS"
    elif (optRuta == 2):
        nombreRuta = "Java"
    elif (optRuta == 3):
        nombreRuta = "NetCore"    
    elif (optRuta == 4):
        return
    borrarPantalla()
    print("Seleccione una base de datos principal y una alternativa")
    pausa()
    optDbP = me.seleccionMenu([1,2,3],4)
    optDbS = me.seleccionMenu([1,2,3],4)
    if (optDbP, optDbS) in opcionesBases:
      rutaModulo.update({"BasesDatos": opcionesBases[(optDbP, optDbS)]})
    
    rutas.get(nombreRuta).get("ruta").update({"modulos": rutaModulo})
    borrarPantalla()
    print('\n'.join(f'{key}: {value}' for key,value in rutas.get(nombreRuta).get('ruta').get('modulos').items()))
    pausa()