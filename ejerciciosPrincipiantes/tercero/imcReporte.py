import os

#Tomaremos los datos del estudiante y usamos el metodo correspondiente para calcular el imc
def ingresarEstudiante(dicImc : dict) -> dict:
    estudiante ={}
    nombre = input('Ingrese el nombre: ')
    edad = verificarDato("la edad", int)
    imc = calcularImc(dicImc)
    estudiante.update({'nombre' : nombre,
                       'edad' : edad,
                       'imc' : imc[0],
                       'categoria imc' : imc[1]})
    return estudiante

#Calculamos el imc y la categoria y retornamos eso como una lista
def calcularImc(dicImc : dict) -> list:
    updateDiccionario = lambda diccionarioUpdate, tipoImcUpdate : diccionarioUpdate.update({tipoImcUpdate : (diccionarioUpdate.get(tipoImcUpdate) + 1)})
    altura = verificarDato('la altura', float)
    peso = verificarDato('el peso', float)
    tipoImc = ["bajo","normal","sobre peso","obesidad I","obesidad II","obesidad III"]
    imc = round((peso/(altura**2)),2)
    categoriaImc = ''
    if(imc < 18.5):
        categoriaImc = tipoImc[0]
        updateDiccionario(dicImc, tipoImc[0])
    elif(imc <= 24.9):
        categoriaImc = tipoImc[1]
        updateDiccionario(dicImc, tipoImc[1])
    elif(imc <= 29.9):
        categoriaImc = tipoImc[2]
        updateDiccionario(dicImc, tipoImc[2])
    elif(imc <= 34.9):
        categoriaImc = tipoImc[3]
        updateDiccionario(dicImc, tipoImc[3])
    elif(imc <= 39.9):
        categoriaImc = tipoImc[4]
        updateDiccionario(dicImc, tipoImc[4])
    else:
        categoriaImc = tipoImc[5]
        updateDiccionario(dicImc, tipoImc[5])

    return [imc,categoriaImc]

#Verficamos que el dato ingresado sea correcto
def verificarDato(dato : str, tipo) -> float:
    while(True):
        try:
            datoInput = tipo(input(f'Ingrese {dato}: '))
        except ValueError:
            os.system('cls')
            print('Ingrese un numero valido, si es real tienen que ser separados con . ')
        else:
            if datoInput >0:
                return datoInput


#Programa principal        
estudiante = {}
contador ={
    "bajo" : 0,
    "normal" : 0,
    "sobre peso" : 0,
    "obesidad I" : 0,
    "obesidad II" : 0,
    "obesidad III" : 0,
}
os.system('clear')
for i in range(0,20):
    estudiante.update({f"estudiante {i}" :ingresarEstudiante(contador)})
    os.system('clear')
    print("""
  Nombre      |      Edad      |     Imc       |    Categoria
-------------------------------------------------------------------
    """)
    for llave, infoCampers in estudiante.items():
        print("  ",end="")
        for key, item in infoCampers.items():
         print(f"{item:<10}",end="       ")
        print("")
    input("Presione enter para continuar...")
    os.system("clear")
for key, item in contador.items():
    print(f"cantidad de estudiantes con categoria {key}: {item}")