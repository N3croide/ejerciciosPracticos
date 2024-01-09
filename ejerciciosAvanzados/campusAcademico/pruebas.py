import os, campers as camp, otrasfunciones as otf, menus as me

def pruebasInicicales(campersNuevos : dict):

    id = otf.comprobarDato("Ingrese el numero de identificacion del camper: ", str)
    camper = camp.buscarCamper(campersNuevos, id)
    otf.borrarPantalla()
    print("Datos del camper\n")
    if (type(camper) == dict and camper.get('estado') != 'aprobado'):
        print("\n".join(f"{key}: {value}" for key, value in camper.items()))
        print("")
        notaP = otf.comprobarDato("Ingrese la nota de la prueba practica: ", float)
        notaT = otf.comprobarDato("Ingrese la nota de la prueba teorica: ", float)
        estado = "reprobado"
        if(((notaP+notaT)/2) >= 60 ):
            estado = "aprobado"
        print(f"El estudiante fue {estado}")
        camper.update({"estado": estado})
        otf.pausa()
    elif(camper.get('estado') == 'aprobado'):
        print(f'El camper {camper.get("nombres")} ya fue aprobado')
        otf.pausa()

def  pruebasModulos(db : dict):
    
    while(True):
        listaModulos = ["FundamentosProgramacion","ProgramacionWeb","ProgramacionFormal","BasesDatos","BackEnd"]
        ruta = me.seleccionMenu([1,2,3,4], 2)
        if (ruta == 1):
            ruta = "NodeJS"
        elif (ruta == 2):
            ruta = "Java"
        elif (ruta == 3):
            ruta = "NetCore"    
        elif (ruta == 4):
            return
        campers = db.get(ruta).get("campers")
        if not campers.keys():
            print("No existen campers asociados a esa ruta.")
            otf.pausa()
            otf.borrarPantalla
            return
        if( not db.get(ruta).get('modulos')):
            otf.borrarPantalla()
            print("Esta ruta no cuenta con modulos registrados.")
            otf.pausa()
            return
        if(not db.get(ruta).get('trainer')):
            otf.borrarPantalla()
            print('Esta ruta no tiene trainer asignado.')
            otf.pausa()
            return
        quicesTrabajos = 0
        teorica = 0
        practica = 0
        modulo = ""
        templateIDNombre = "{ID:^10}|{nombres:^20}"
        
        print(templateIDNombre.format(ID = "Id",nombres = "Nombre"))
        for key in campers.keys():
            print(templateIDNombre.format(**campers.get(key)))

        id = otf.comprobarDato("Ingrese el id del camper: ", str)
        if (type(camp.buscarCamper(campers, id)) == dict):
            otf.borrarPantalla()
            for i, item in enumerate(listaModulos):
                print(i +1 ,". ",item)
            optModulo = otf.comprobarDato("Seleccione un modulo: ",int) - 1
            while(optModulo not in [0,1,2,3]):
                optModulo = otf.comprobarDato("Ingrese un numero de modulo correcto: ", int) - 1
            modulo = listaModulos[optModulo]
            teorica  = (otf.comprobarDato("Ingrese el la nota de la prueba teorica: ", float) * 0.3)
            practica  = (otf.comprobarDato("Ingrese el la nota de la prueba practica: ", float) * 0.6)
            while(True):
                quicesTrabajos = (quicesTrabajos  + (otf.comprobarDato("Ingrese la nota de de quiz o trabajo: ", float)))  * 0.1
                if otf.comprobarDato("Desea ingresar otra nota de quices y trabajos ? S(si) o N(no)", str) in "Nn":
                    break
            notaModulo = teorica  + practica + quicesTrabajos
            campers.get(id).get("notas").update({modulo: notaModulo})
            notasAcumuladas = []
            if modulo != listaModulos[0]:
                for i,modulo in range(enumerate(listaModulos),-1,-1):
                    notasAcumuladas.append(campers.get(id).get("notas").get(modulo))
            
            else:
                notasAcumuladas.append(notaModulo)
            promedioNotasTotales = sum(notasAcumuladas) / len(notasAcumuladas)
            db.get(ruta).get("campers").get(id).get("notas").update({modulo: notaModulo})
            if notaModulo >= 60:
                print(f"El camper {campers.get(id).get('nombres')} aprobo el modulo de {modulo} con una nota final de {notaModulo}")
                db.get(ruta).get("modulos").get(modulo).get("resultados").update({"aprobados":( (db.get(ruta).get("modulos").get(modulo).get("resultados").get("aprobados")) + 1 )})
                otf.pausa()
            if notaModulo < 60:
                print(f"El camper {campers.get(id).get('nombres')} reprobo el modulo de {modulo} con una nota final de {notaModulo}")
                db.get(ruta).get("modulos").get(modulo).get("resultados").update({"reprobados":( (db.get(ruta).get("modulos").get(modulo).get("resultados").get("reprobados")) + 1 )})
                otf.pausa()

            if promedioNotasTotales <60:
                db.get(ruta).get("campers").get(id).update({"estado":"bajo rendimiento"})
                otf.pausa()
        else:
            print("Esa id no existe o la lista esta vacia")    
            otf.pausa()
        otf.borrarPantalla()
        if(otf.comprobarDato("Desea ingresar la nota de otro estudiante? S(si) o N(no)", str) in "Nn"):
            break
        
