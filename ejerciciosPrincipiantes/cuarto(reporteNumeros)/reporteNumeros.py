import os
def actualizarReporte(reporte : dict, totalNumeros : list):
    numeroMenor10 = 0
    numeroEntre20_50 = 0
    numeroMayor100 = 0
    numerosPares = list(filter((lambda par : par % 2 == 0),totalNumeros))
    numerosImpares = list(filter((lambda par : par % 2 != 0),totalNumeros))
    numeroMenor10 = len(list(filter((lambda num: 1 if num < 10 else 0),totalNumeros)))
    numeroEntre20_50 = len(list(filter((lambda num: 1 if (num > 20 and num< 50) else 0),totalNumeros)))
    numeroMayor100 = len(list(filter((lambda num: 1 if num > 100 else 0),totalNumeros)))
    reporte.update({"total de numeros" : (reporte.get("total de numeros") + 1)})
    if(len(numerosPares) != 0):
        reporte.update({"promedio de numeros pares": round((sum(numerosPares)/len(numerosPares)),2)})
    if(len(numerosImpares) != 0):
        reporte.update({"promedio de numeros impares" :round((sum(numerosImpares)/len(numerosImpares)),2)})
    reporte.update({"total de numeros pares" : len(numerosPares)})
    reporte.update({"numeros menores que 10" : numeroMenor10})
    reporte.update({"numeros entre 20 y 50" : numeroEntre20_50})
    reporte.update({"numeros mayores que 100" : numeroMayor100})
    

def verificarNumero() -> int:
    while(True):
        try:
            numero = int(input("Ingrese el numero, si quiere salir ingrese un numero negativo: "))
            os.system("clear")
        except ValueError:
            print("Ingrese un numero entero positivo")
        else:
            return numero


isActive = True
numero = 0
totalNumeros = []
reporteNumeros = {
    "total de numeros" : 0,
    "total de numeros pares" : 0,
    "promedio de numeros pares" : 0,
    "promedio de numeros impares" : 0,
    "numeros menores que 10" : 0,
    "numeros entre 20 y 50" : 0,
    "numeros mayores que 100" : 0
}
while(isActive):
    numero = verificarNumero()
    if (numero > 0):
        totalNumeros.append(numero)
        actualizarReporte(reporteNumeros, totalNumeros)
    elif(numero < 0):
        isActive = False
for key, item in reporteNumeros.items():
    print(f"{key} : {item}")
