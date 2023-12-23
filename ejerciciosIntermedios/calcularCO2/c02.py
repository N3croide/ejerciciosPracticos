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
    nombre = input("Ingrese el nombre de la dependencia") 
    dependencia = dp.buscarDependencia(dependencias, nombre)
    consumoDispositivos = 0.0
    consumoElectricidad = 0
    consumoTransporte = 0
    opt = me.menuConsumo
    if (opt == 1):
        isActive = "s"
        while(isActive in "sS"):

            dispoPo = comprobarDato(input("Ingrese la potencia del dispositivo en W"),float)
            dispoUse = comprobarDato(input("Ingrese el tiempo de uso del dispositivo"),float)
            consumoDispositivos += ((dispoPo*dispoUse)/1000)
            isActive = input("Desea ingresar otro dispositivo ? S(si) o presione cualquier tecla para continuar")
    elif(opt == 2):
        tipoCombustible = input("Tipos de energia\n1. Energia Hidraulica\n2. Energia Termica\n3.Energia Renovable ")
        consumoTransporte = comprobarDato(input("Ingrese la cantidad de km recorridos"),float) * ((factoresEmimsion.get("transporte"))[tipoCombustible-1])

    elif(opt == 3):
        tipoElectricidad = input("Tipos de energia\n1. Energia Hidraulica\n2. Energia Termica\n3.Energia Renovable ")
        if(input("El consumo es mensual ? S(si) o presione cualquier tecla para no") != "Ss"):
            consumoNoMensual = comprobarDato(input("Ingrese el consumos en kWh: "),float)
            cantidadMeses = comprobarDato(input("Ingrese el periodo de facturacion de esa cantidad: "),int)
            consumoElectricidad = (consumoNoMensual/cantidadMeses) * ((factoresEmimsion.get("electricidad"))[tipoElectricidad-1])
        else:
            consumoElectricidad = (comprobarDato(input("Ingrese el consumos en kWh: "),float)) * ((factoresEmimsion.get("electricidad"))[tipoElectricidad-1])
    elif(opt == 4):
        return
    dependencia.get(nombre).update({"electricidad" : consumoElectricidad})
    dependencia.get(nombre).update({"transporte" : consumoTransporte})
    dependencia.get(nombre).update({"dispositivos" : consumoDispositivos})


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
                dato = tipo(input("ingrese una valor valido"))
            except ValueError:
                print(f"El dato debe ser de tipo {tipoUsuario}")
    else:
        return dato