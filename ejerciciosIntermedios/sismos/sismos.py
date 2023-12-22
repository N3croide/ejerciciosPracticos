import os
borrarPantalla = lambda : os.system("cls")
pausa = lambda : input("Presione cualquier tecla para continuar...")

def registrarSismo(ciudad : list) -> list:
    isActive = "s"
    while(isActive in "sS"):
        borrarPantalla()
        try:
            sismo = float(input("Ingrese la magnitud del sismo: "))
        except ValueError:
            print("Ingrese un valor valido ejem 2.1")
            pausa()
        else:
            ciudad[1].append(sismo)
            print(ciudad)
            isActive = input("Desea realizar otro registro a la misma ciudad ? S(si) N(no) ")

def buscarSismo(ciudad : list):
    borrarPantalla()
    print(f"Cantidad de sismos de {ciudad[0]} son {len(ciudad[1])} y fueron de las siguientes magnitudes {ciudad[1]}")
    pausa()

def informeSismos(ciudades : list):
    promedioSismos = []
    if len(ciudades) < 5:
        print("Porfavor ingrese las cinco(5) ciudades.")
        return
    for i in range(len(ciudades)-1):
        ciudad1 = ciudades[i]
        ciudad2 = ciudades[i + 1]
        if (len(ciudad1[1]) != len(ciudad2[1])):
            print("Todas las ciudades deben tener la misma cantida de sismos regitrado.")
            pausa()
            return
        else:
            promedioSismos.append([ciudad1[0],(sum(ciudad1[1])/len(ciudad1[1]))])
    
    for item in promedioSismos:
        nombreCiudad = item[0]
        promedioCiudad = item[1]
        if(promedioCiudad <= 2.5):
            print(f"El riesgo de {nombreCiudad} es Amarillo(Sin riego), su promedio de sismos es: {promedioCiudad}")
        elif(promedioCiudad <= 4.5):
            print(f"El riesgo de {nombreCiudad} es Naranja(Riesgo medio), su promedio de sismos es: {promedioCiudad}")
        elif(promedioCiudad > 4.5):
            print(f"El riesgo de {nombreCiudad} es Rojo(Riesgo alto), su promedio de sismos es: {promedioCiudad}")
    pausa()