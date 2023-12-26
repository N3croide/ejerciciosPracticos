import os,menus as me, torneo as tn

borrarPantalla = lambda : os.system('cls')
pausa = lambda : os.system('pause')

jugadores = {
    'novato': {},
    'intermedio': {},
    'avanzado': {}
}

ganadores = {}

while(True):
    borrarPantalla()
    optMenu = me.seleccionMenu()
    if(optMenu == 1):
        tn.registrarJugador(jugadores)
    elif(optMenu == 2):
        categoria = me.seleccionCategoria()
        if (len(jugadores.get(categoria)) >= 1) :
            tn.iniciarJuego(categoria, jugadores.get(categoria), ganadores)
        else:
            print("Deben haber almenos 5 inscritos en la categoria para iniciar el torneo.")
            pausa()
    elif(optMenu == 3):
        templateNombres = "{id:^4}|{jugador:^10}|"
        templatePuntos = "{PJ:^4}|{PG:^4}|{PP:^4}|{PA:^4}|{TP:^4}"
        print(templateNombres.format(id =  "Id", jugador = "Nombre"),end= "")
        print(templatePuntos.format(PJ = "PJ", PG = "PG", PP = "PP", PA = "PA", TP = "TP"))
        print("+++++++++++++++++++++++++++++++++++++++++")
        for idJugadores in jugadores.values():
            for idj, info in idJugadores.items():
                puntosJugador = info.get("puntajes")
                print(templateNombres.format(id = idj, jugador = info.get("jugador")),end="")
                print(templatePuntos.format(**puntosJugador))
        pausa()
                
    elif(optMenu == 4):
        for cate,jugador in ganadores:
            print(f"El ganador de la categoria {cate} es {jugador.get('jugador')} ")
    elif(optMenu == 5):
        break