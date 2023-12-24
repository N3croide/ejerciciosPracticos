import os
pausa = lambda : os.system('pause')
borrarPantalla = lambda : os.system('cls')

menu = """1. Registrar producto
2. Visualizacion de productos
3. Actualizacion de stock
4. Informe de productos criticos
5. Calculo de ganancia potencial
6. Salir"""

def registrarProd(producto : dict) -> dict:
    while(True):
        codigo = comprobarDato(("Ingrese el codigo del producto: "), int)
        if (codigo in producto):
            print("El codigo del producto ya existe, porfavor ingrese un codigo diferente")
        else:
            nombre = input("Ingrese el nombre del producto: ")
            valorCompra = comprobarDato(("Valor de compra del producto: "), float)
            valorVenta = comprobarDato(("Valor de venta del producto: "), float)
            stockMin = comprobarDato(("Stock minimo del producto: "), int)
            stockMax = comprobarDato(("Stock maximo del producto: "), int)
            proveedor = input("Nombre del proveedor: ")
            prod = {
                "codigo" : codigo,
                "nombre" : nombre,
                "valor de compra" : valorCompra,
                "valor de venta" : valorVenta,
                "stock minimo" : stockMin,
                "stock maximo" : stockMax,
                "proveedor" : proveedor
            }
            return {f"{codigo}" : prod}

def verProd(prods : dict):
    print("|  codigo   |  nombre  |  valor de compra  |  valor de venta  |  stock min  |  proveedor  |")
    for item in prods.values():
        for valor in item.values():
            print(valor<15)

def comprobarDato (cadena, tipo):
    tipoUsuario = ""

    if(tipo == int):
        tipoUsuario = "entero"
    elif(tipo == float):
        tipoUsuario = "real"

    try:
        dato = tipo(input(cadena))
    except ValueError:
        while(type(dato) != tipo):
            try:
                dato = tipo(input(cadena))
            except ValueError:
                print(f"El dato debe ser de tipo {tipoUsuario}")
        return dato
    else:
        return dato