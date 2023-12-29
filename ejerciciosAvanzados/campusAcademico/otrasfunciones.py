import os
def pausa():
    os.system('pause')


def borrarPantalla():
    os.system('cls')


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
