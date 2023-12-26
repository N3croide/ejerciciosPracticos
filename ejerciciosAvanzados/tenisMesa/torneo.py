import os, menus as me
borrarPantalla = lambda : os.system('cls')
pausa = lambda : os.system('pause')

def registrarJugador(jugadores : dict):
    borrarPantalla()
    categoria = ""
    id = 0
    while(True):
        print("""Categoria          Edad permitida
    Novato     --- entre 15 y 16
    Intermedio --- entre 17 y 20
    Avanzado   --- mayor a 20
        """)
        categoria = me.seleccionCategoria()
        edad = comprobarDato("Ingrese la edad del jugador: ", int)
        if (categoria == "novato" and  edad in [15,16] ):
            break
        elif (categoria == "intermedio" and  edad <= 20 and edad >= 17 ):
            break
        elif (categoria == "novato" and  edad >20):
            break
        else:
            borrarPantalla()
            print("La edad del jugador en menor a 15 o no es admitido en esta categoria")
            pausa()
    while(True):
        id = comprobarDato("Ingerse el id del jugador: ",int)
        if id not in jugadores.get(categoria):
            break
        else:
            print("Ese id ya existe, porfavor ingrese un id diferente.")
            pausa()
    nombre = comprobarDato("Ingrese el nombre del jugador: ", str)
    jugadores.get(categoria).update({id : {
        "id": id,
        "jugador": nombre,
        "puntajes":{
            "PJ":0,
            "PG":0,
            "PP":0,
            "PA":0,
            "TP":0,
        }
    }})
    print(jugadores.get(categoria).get(id))
    pausa()

def iniciarJuego(categoria : str, jugadores : dict, ganadores : dict):

    partidos = set()
    for j1Id,j1Value in jugadores.items():
        for j2Id, j2Value in jugadores.items():
            if ( (j2Id != j1Id) and ((j1Id, j2Id) not in partidos) and ((j2Id, j1Id) not in partidos) ):
                j1Puntajes = j1Value.get("puntajes")
                j2Puntajes = j2Value.get("puntajes")
                partidos.add((j1Id, j2Id))
                borrarPantalla()
                print(f"========== Partido del jugador {j1Value.get('jugador')} contra el jugador {j2Value.get('jugador')} ==========\n")
                puntosj1 = comprobarDato(f"Ingrese los puntos de {j1Value.get('jugador')}: ", int)
                puntosj2 = comprobarDato(f"Ingrese los puntos de {j2Value.get('jugador')}: ", int)

                if (puntosj1 > puntosj2):
                    j1Puntajes.update({"PA": (puntosj1 - puntosj2) })
                    j1Puntajes.update({"PG": (j1Puntajes.get("PG") + 1) })
                    j1Puntajes.update({"TP": (j1Puntajes.get("TP") + 2) })

                    j2Puntajes.update({"PP": (j2Puntajes.get("TP") + 1) })
                else:
                    j2Puntajes.update({"PA": (puntosj2 - puntosj1) })
                    j2Puntajes.update({"PG": (j2Puntajes.get("PG") + 1) })
                    j2Puntajes.update({"TP": (j2Puntajes.get("TP") + 2) })

                    j1Puntajes.update({"PP": (j1Puntajes.get("PP") + 1) })

                j1Puntajes.update({"PJ": (j1Puntajes.get("PJ") + 1)})
                j2Puntajes.update({"PJ": (j2Puntajes.get("PJ") + 1)})
    ganador(categoria, jugadores, ganadores)

def ganador(categoria : str, jugadores : dict, ganadorCat : dict):
    ganador = {"jugador" : "",
               "puntajes": {}}
    empate = {}
    for j1Id,j1Value in jugadores.items():
        for j2Id, j2Value in jugadores.items():
            if (j1Id != j2Id):
                if ( (j1Value.get("puntajes").get("TP")) > (j2Value.get("puntajes").get("TP")) ):
                    ganador.update({"jugador": j1Value.get("jugador"),
                                    "puntajes": j1Value.get("puntajes")})
                elif( (j1Value.get("puntajes").get("TP")) < (j2Value.get("puntajes").get("TP")) ):
                    ganador.update({"jugador": j2Value.get("jugador"),
                                    "puntajes": j2Value.get("puntajes")})
                else:
                    if ( (j1Value.get("puntajes").get("PA")) > (j2Value.get("puntajes").get("PA")) ):
                        ganador.update({"jugador": j1Value.get("jugador"),
                                        "puntajes": j1Value.get("puntajes")})
                    elif( (j1Value.get("puntajes").get("PA")) < (j2Value.get("puntajes").get("PA")) ):
                        ganador.update({"jugador": j2Value.get("jugador"),
                                        "puntajes": j2Value.get("puntajes")})
                    else:
                        empate.update({j1Id : j1Value, j2Id : j2Value})

    templatePuntos = "{PJ:^15}|{PG:^15}|{PP:^15}|{PA:^15}|{TP:^15}"
    borrarPantalla()
    if not ganador["jugador"]:
        print("Ocurrio un empate tanto en puntos a favor y puntos totales, se realizara un partido de desempate")
        pausa()
        iniciarJuego(empate)
    else:
        print(f"El ganador es {ganador.get('jugador')} con una puntuacion de: ")
        print(templatePuntos.format(PJ = "Partidos jugados", PG = "Patidos Ganados", PP = "Partidos perdidos", PA = "Puntos a favor", TP = "Puntos totales"))
        print(templatePuntos.format(**ganador.get("puntajes")))
        ganadorCat.update({categoria: ganador})
        pausa()

def comprobarDato (cadena, tipo):
    tipoUsuario = ""
    dato =""
    
    if(tipo == int):
        tipoUsuario = "entero"
    elif(tipo == float):
        tipoUsuario = "real"
    elif(tipo == str):
        tipoUsuario = "texto"
    try:
        dato = tipo(input(f"{cadena}"))
    except ValueError:
        while(type(dato) != tipo):
            try:
                print(f"El dato debe ser de tipo {tipoUsuario}")
                dato = tipo(input(cadena))
            except ValueError:
                borrarPantalla()
        return dato
    else:
        return dato