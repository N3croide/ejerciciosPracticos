import otrasfunciones as otf, menus as me

def registrarCamper(campersNuevos : dict) -> dict:
    otf.borrarPantalla()
    id = otf.comprobarDato("Ingrese la identificacion: ",  str)
    while(len(str(id)) < 9): id = otf.comprobarDato("Ingrese una identificacion valida de 10 digitos: ", str)
    nombre = otf.comprobarDato("Ingrese el nombre: ",  str)
    apellidos = otf.comprobarDato("Ingrese el apellido: ",  str)
    direccion = otf.comprobarDato("Ingrese la dirección: ",  str)
    acudiente = otf.comprobarDato("Ingrese el nombre del acudiente: ",  str)

    celular = otf.comprobarDato("Ingrese el telefono celular: ", int)
    while len(str(celular)) < 9: celular = otf.comprobarDato("ingrese un nummero celular valido: ", int)

    fijo = otf.comprobarDato("Ingrese el telefono fijo: ", int)
    while len(str(fijo)) < 6: fijo = otf.comprobarDato("ingrese un telefono fijo valido: ", int)
    
    teléfonos = {"celular":celular,"fijo":fijo}
    otf.borrarPantalla()
    camper = {"ID": id,
              "nombres": nombre,
              "apellidos": apellidos,
              "direccion": direccion,
              "acudiente": acudiente,
              "telefonos": teléfonos,
              "estado": "inscrito",
              "notas":{
                  "FundamentosProgramacion":0,
                  "ProgramacionWeb":0,
                  "ProgramacionFormmal":0,
                  "BasesDatos":0,
                  "BackEnd":0
              }}
    
    print("\n".join(f"{key}: {value}" for key, value  in camper.items()))
    otf.pausa()
    campersNuevos.update({id: camper})

def buscarCamper(campers: dict, id : str) -> dict:
    if id in campers.keys():
        return campers.get(id)
    else:
        print("No se encontro el camper con ese numero de identificacion. ")
        otf.pausa()

def matriculaCamers(db: dict, campersNuevos : dict, salones : dict):
    campersAprobados={}
    campersAprobados.update({key: value for key, value in campersNuevos.items() if campersNuevos.get(key).get("estado") == "aprobado"})
    templateIDNombre = "{ID:^10}|{nombres:^20}"
    while(True and len(campersAprobados) != 0):
        print(templateIDNombre.format(ID = "Id",nombres = "Nombre"))
        for key in campersAprobados.keys():
            print(templateIDNombre.format(**campersAprobados.get(key)))

        id = otf.comprobarDato("Ingrese el id del camper: ", str)
        if id in campersAprobados.keys():

            nombreRuta = ""
            fechaIn = otf.comprobarDato("Ingrese la fecha de inicio del camper: ", str)
            fechaFin = otf.comprobarDato("Ingrese la fecha de finalizacion del camper: ", str)
            campersAprobados.get(id).update({"fechaInicio": fechaIn, "fechaFin": fechaFin})
            print("\nLista de areas de entrenamiento\n")
            for key in salones.keys():
                print(f"{key}. {salones.get(key).get('nombre')} campers asignados: {salones.get(key).get('campers')}")
            salon = otf.comprobarDato("Seleccion un salon: ",str)
            while (salones.get(salon).get("campers") > 33):
                otf.borrarPantalla()
                print("El salon llego a su maxima capacidad, sera redirigido al menu principal")
                otf.pausa()
                return
            salones.get(salon).update( {"campers": (salones.get(salon).get("campers") + 1) })

            print("\nA continuacion seleccione la ruta del camper.")
            otf.pausa()
            optRuta = me.seleccionMenu([1,2,3,4], 2)
            if (optRuta == 1):
                nombreRuta = "NodeJS"
            elif (optRuta == 2):
                nombreRuta = "Java"
            elif (optRuta == 3):
                nombreRuta = "NetCore"    
            elif (optRuta == 4):
                return
            db.get(nombreRuta).get("campers").update({id: campersAprobados.get(id)})
            print(f"Camper {campersAprobados.get(id).get('nombres')} asignado a la ruta {nombreRuta}")
            campersAprobados.pop(id)
            campersNuevos.pop(id)
        else:
            print("No existe ese id.")
            otf.pausa()
        if (otf.comprobarDato("Quiere matricular otro camper ? S(si) o N(no)",str) in "nN" ):
            return
    if(len(campersAprobados) == 0):
        print("No hay ningun camper nuevo aprobado")
        otf.pausa()

def mostrarCampers(estado : str, campers : dict):
        estadoP = f"CON ESTADO {estado}"
        templateCamper = "{ID:^15}|{nombres:^15}|{apellidos:^15}|{direccion:^15}|{acudiente:^15}|{estado:^15}|"
        templateCelFijo = "{celular:^15}|{fijo:^15}"
        print(f"===================================================CAMPERS{estadoP.upper() if estado != '' else ''}====================================================\n")
        print(templateCamper.format(ID="ID",nombres="Nombres",apellidos="Apellidos",direccion="Direccion",acudiente="Acudiente",estado="Estado"),end="")
        print(templateCelFijo.format(celular = "Celular", fijo = "Fijo"))
        for id in campers.keys():
            if(campers.get(id).get("estado") == estado):
                print(templateCamper.format(**(campers.get(id))),end="")
                print(templateCelFijo.format(**(campers.get(id).get("telefonos"))))
            elif(estado == ""):
                print(templateCamper.format(**(campers.get(id))),end="")
                print(templateCelFijo.format(**(campers.get(id).get("telefonos"))))
        print("")
        otf.pausa()