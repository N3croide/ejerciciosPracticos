def actualizarReporte(reporte : dict, numero : int, totalNumeros : list):
    reporte.update({"total de numeros" : (reporte.get("total de numeros") + 1)})
    if((numero % 2) == 0):
        reporte.update({"total de numeros pares" : (reporte.get("total de numeros pares") + 1)})
    
    

def verificarNumero() -> int:
    while(True):
        try:
            numero = int(input("Ingrese el numero: "))
        except ValueError:
            print("Ingrese un numero entero positivo")
        else:
            return numero


isActive = True
numero = 0
totalNumeros = []
reporteNumeros = {
    "total de numeros" : 0,
    "total de numero pares" : 0,
    "promedio de los numeros pares" : 0,
    "promedio de los numeros impares" : 0,
    "cuantos numeros son menores que 10" : 0,
    "cuantos numeros estan entre 20 y 50" : 0,
    "cuantos numeros son mayores que 100" : 0
}
while(isActive):
    numero = verificarNumero()
    if (numero > 0):
        actualizarReporte(reporteNumeros, numero, totalNumeros)
        totalNumeros.append(numero)
    elif(numero < 0):
        isActive = False
print(reporteNumeros)