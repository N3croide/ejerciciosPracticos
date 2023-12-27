import os

pausa = lambda : os.system('pause')
borrarPantalla = lambda : os.system('cls')

menuPrincipal = "1. Registrar camper\n2. Prueba inicial\n3. Crear rutas\n4. Registrar Entrenador\n5. Gestor de matriculas\n6. Prueba de modulo\n7. Reportes\n8. Salir"

menuRutas = "1. NodeJS\n2. Java\n3. NetCore\n4. Atras"

menuReportes = """1. Listar los campers que se encuentren en estado de inscrito.
2. Listar los campers que aprobaron el examen inicial.
3. Listar los entrenadores que se encuentran trabajando con campuslands.
4. Listar los estudiantes que cuentan con bajo rendimiento.
5. Listar los campers y entrenador que se encuentren asociados a una ruta de entrenamiento.
6. Campers aprobador y perdiddos por modulo.
7. Atras"""

menuDB =  "1. MySql\n2. MongoDB\n3. Postgresql"

def seleccionMenu(opcionesValidas : list, optMenu: int) -> int:
    menu = ""
    if(optMenu == 1):
        menu = menuPrincipal
    elif(optMenu == 2):
        menu = menuRutas
    elif(optMenu == 3):
        menu = menuReportes
    elif(optMenu == 4):
        menu = menuDB
    while(True):
        borrarPantalla()
        print(menu)
        opt = comprobarDato('Seleccione una opcion: ', int)
        if (opt in opcionesValidas):
            return opt
        else:
            print("Seleccione una opcion correcta.")
            pausa()
            borrarPantalla()

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
    