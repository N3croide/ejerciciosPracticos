import os
pausa = lambda : os.system('pause')
borrarPantalla = lambda : os.system('cls')

def comprobarDato (cadena, tipo):
    tipoUsuario = ''
    dato =''
    if(tipo == int):
        tipoUsuario = 'entero'
    elif(tipo == float):
        tipoUsuario = 'real'
    elif(tipo == str):
        tipoUsuario = 'cadena'
    
    while(True):
        try:
            dato = tipo(input(f'{cadena}'))
        except ValueError:
            print(f'El dato debe ser de tipo {tipoUsuario}')
            continue
        if(tipo == str and not dato.strip()):
            borrarPantalla()
            print(f"El campo no puede estar vacio")
            continue
        return dato
 
def registrarCamper() -> dict:
    borrarPantalla()
    id = comprobarDato("Ingrese la identificacion: ",  int)
    while(len(str(id)) < 9): id = comprobarDato("Ingrese una identificacion valida de 10 digitos: ", int)

    nombre = comprobarDato("Ingrese el nombre: ",  str)
    apellidos = comprobarDato("Ingrese el apellido: ",  str)
    direccion = comprobarDato("Ingrese la dirección: ",  str)
    acudiente = comprobarDato("Ingrese el nombre del acudiente: ",  str)

    celular = comprobarDato("Ingrese el telefono celular: ", int)
    while len(str(celular)) < 9: celular = comprobarDato("ingrese un nummero celular valido: ", int)

    fijo = comprobarDato("Ingrese el telefono fijo: ", int)
    while len(str(fijo)) < 9: celular = comprobarDato("ingrese un telefono fijo valido: ", int)
    
    teléfonos = {"Celular":celular,"fijo":fijo}
    camper = {"ID": id,
              "nombre": nombre,
              "apellidos": apellidos,
              "direccion": direccion,
              "acudiente": acudiente,
              "telefonos": teléfonos,
              "estado": "inscrito"}
    print("\n".join(f"{key}: {value}" for key, value  in camper.items()))
    pausa()
    return(camper)

def comprobarCamper():
    pass