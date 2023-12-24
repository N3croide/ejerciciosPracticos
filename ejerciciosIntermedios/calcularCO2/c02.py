import os, dependencias as dp, menus as me
pausa = lambda : os.system('pause')
borrarPantalla = lambda : os.system('cls')

factoresEmimsion = {
    "transporte": [
        2.3,
        3.0
    ],
    "electricidad": [
        0,
        0.5,
        0.1
    ]
}

def registrarConsumo(dependencias: dict):
    nombre = input("Ingrese el nombre de la dependencia: ") 
    dependencia = dp.buscarDependencia(dependencias, nombre)
    if(dependencia == None):
        print(f"No se encontro la dependecia con nombre {nombre}")
        pausa()
        return
    consumoDispositivos = 0.0
    consumoElectricidad = 0
    consumoTransporte = 0
    while(True):
        borrarPantalla()
        opt = me.mostrarMenuConsumo()
        if (opt == 1):
            isActive = "s"
            while(isActive in "sS"):

                dispoPo = comprobarDato(input("Ingrese la potencia del dispositivo en W: "),float)
                dispoUse = comprobarDato(input("Ingrese el tiempo de uso del dispositivo: "),float)
                consumoDispositivos += ((dispoPo*dispoUse)/1000)
                isActive = input("Desea ingresar otro dispositivo ? S(si) o N(no): ")
            print(f"Emision de co2 por dispositivos: {consumoDispositivos}")
            pausa()
        elif(opt == 2):
            borrarPantalla()
            tipoCombustible = comprobarDato(input("Tipos de combustible\n1. Gasolina\n2. Diesel\nSeleccion una opcion: "),int)
            consumoTransporte = comprobarDato(input("Ingrese la cantidad de km recorridos: "),float) * ((factoresEmimsion.get("transporte"))[tipoCombustible-1])
            print(f"Emision de co2 por combustibles: {consumoTransporte}")
            pausa()

        elif(opt == 3):
            borrarPantalla()
            tipoElectricidad = comprobarDato(input("Tipos de energia\n1. Energia Hidraulica\n2. Energia Termica\n3. Energia Renovable\nSeleccione una opcion:  "), int)
            if(input("El consumo es mensual ? S(si) o N(no)") not in "Ss"):
                consumoNoMensual = comprobarDato(input("Ingrese el consumo en kWh: "), float)
                cantidadMeses = comprobarDato((input("Ingrese el periodo de facturacion de esa cantidad: ")), int)
                consumoElectricidad = (consumoNoMensual/cantidadMeses) * ((factoresEmimsion.get("electricidad"))[tipoElectricidad-1])
            else:
                consumoElectricidad = (comprobarDato(input("Ingrese el consumos en kWh: "), float)) * ((factoresEmimsion.get("electricidad"))[tipoElectricidad-1])
            print(f"Emisino de co2 por electricidad: {consumoElectricidad}")
            pausa()
        elif(opt == 4):
            print(f"Emision de la dependencia {nombre}: {dependencia.get(nombre)}")
            pausa()
            return
        dependencia.get(nombre).update({"electricidad" : consumoElectricidad})
        dependencia.get(nombre).update({"transporte" : consumoTransporte})
        dependencia.get(nombre).update({"dispositivos" : consumoDispositivos})
        dependencia.get(nombre).update({"total" : (consumoElectricidad + consumoTransporte + consumoDispositivos)})
        
def mostrarCO2(dependencias : dict):
    totalCO2 = 0.0
    for key, item in dependencias.items():
        print(f"\nConsumo co2 de la dependencia {key}:")
        for tipoCo2, cantidadCo2 in item.items():
            if(tipoCo2 == "total"):
                totalCO2 =+ cantidadCo2
            print(f"{tipoCo2}: {cantidadCo2:.2f}",end=" -- ")

    print(f"\nEl total producido es de {totalCO2:.2f}")
    pausa()

def mayoCO2(dependencias : dict):
    mayor = 0.0
    nombreDep = ""
    for key, item in dependencias.items():
        totalDep = item.get("total")
        if mayor < totalDep:
            mayor = totalDep
            nombreDep = key
    print(f"La dependencia con mayor emision de co2 es {nombreDep} con un total de {mayor:.4f}")
    pausa()

def comprobarDato (dato, tipo):
    tipoUsuario = ""
    if(tipo == int):
        tipoUsuario = "entero"
    elif(tipo == float):
        tipoUsuario = "real"
    try:
        dato = tipo(dato)
    except ValueError:
        while(type(dato) != tipo):
            try:
                dato = tipo(input("ingrese una valor valido: "))
            except ValueError:
                print(f"El dato debe ser de tipo {tipoUsuario}")
        return dato
    else:
        return dato