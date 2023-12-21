import os

#Tomaremos los datos del estudiante y usamos el metodo correspondiente para calcular el imc
def ingresarEstudiante() -> dict:
    estudiante ={}
    nombre = input('Ingrese el nombre: ')
    edad = input('Ingrese  la  edad: ')
    imc = calcularImc()
    estudiante.update({'nombre' : nombre,
                       'edad' : edad,
                       'imc' : imc[0],
                       'categoria imc' : imc[1]})
    return estudiante

#Calculamos el imc y la categoria y retornamos eso como una lista
def calcularImc() -> list:
    altura = verificarDato('la altura')
    peso = verificarDato('el peso')
    imc = round((peso/(altura**2)),2)
    categoriaImc = ''
    if(imc < 18.5):
        categoriaImc = 'Bajo' 
    elif(imc <= 24.9):
        categoriaImc = 'Normal' 
    elif(imc <= 29.9):
        categoriaImc = 'Sobre Peso' 
    elif(imc <= 34.9):
        categoriaImc = 'Obesidad I' 
    elif(imc <= 39.9):
        categoriaImc = 'Obesidad II' 
    else:
        categoriaImc = 'Obesidad III' 

    return [imc,categoriaImc]

#Verficamos que el dato ingresado sea correcto
def verificarDato(dato : str) -> float:
    while(True):
        try:
            datoInput = float(input(f'Ingrese {dato}: '))
        except ValueError:
            os.system('cls')
            print('Ingrese un numero real separado por punto ejem: (2.4)')
        else:
            return datoInput
        
#Programa principal        
isActive =  "s"
estudiante = {}
os.system('cls')
while(isActive in "sS"):
    estudiante.update(ingresarEstudiante())
    os.system('cls')
    for key, item in estudiante.items():
        print(f"{key}: {item}")
    isActive = input("Desesa ingresar otro estudiante ? S(si) N(no)\n")
    os.system("cls")