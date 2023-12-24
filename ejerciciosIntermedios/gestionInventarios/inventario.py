import os
pausa = lambda : os.system('pause')
borrarPantalla = lambda : os.system('cls')

menu = """1. Registrar producto
2. Visualizacion de productos
3. Actualizacion de stock
4. Informe de productos criticos
5. Calculo de ganancia potencial
6. Salir"""


def seleccionMenu() -> int:
    while(True):
        try:
            print(menu)
            optMenu = int(input("Seleccione una opcion: "))
        except ValueError:
            print("Ingrese un valor valido.")
            pausa()
        else:
            if (optMenu in [1,2,3,4,5,6]):
                return optMenu
            else:
                borrarPantalla()
                print("Ingrese un numero del 1 al 6.")
                pausa()

def registrarProd(producto : dict) -> dict:
    while(True):
        borrarPantalla()
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
            stock = comprobarDato("Cantidad del producto: ",int)
            prod = {
                "codigo" : codigo,
                "nombre" : nombre,
                "valorCompra" : valorCompra,
                "valorVenta" : valorVenta,
                "stockMinimo" : stockMin,
                "stockMaximo" : stockMax,
                "proveedor" : proveedor,
                "stock": stock
            }
            print(prod)
            pausa()
            return {codigo : prod}

def verProd(prods : dict):
    template = "{codigo:^10}|{nombre:^17}|{stock:^10}|{valorCompra:^20}|{valorVenta:^20}|{stockMinimo:^14}|{stockMaximo:^14}|{proveedor:^15}|"
    print (template.format(codigo = "codigo", nombre = "nombre",stock= "Cantidad", valorCompra= "valor de compra",
                            valorVenta= "valor de venta",stockMinimo = "stock minimo", stockMaximo= "stock maximo", proveedor= "proveedor"))
    print("----------|-----------------|----------|--------------------|--------------------|--------------|--------------|---------------|")
    for item in prods.values():
        print(template.format(**item))

def actualizacionStock(productos : dict ):
    codigo = comprobarDato("Ingrese el codigo del producto: ",int)
    cantidad = 0
    prod = dict()
    stockActual = 0
    print(productos.keys())
    if (codigo in productos.keys()):
        prod = productos.get(codigo)
        stockActual = prod.get("stock")
        print(f"Cantidad del producto actualmente: {stockActual}")
        while(True):
            borrarPantalla()
            opt = comprobarDato("1. Agregar al stock\n2. Restar al stock\nSeleccione una opcion: ",int)
            cantidad = comprobarDato("Ingrese la cantidad a actualizar: ",int)
            if (opt == 1):
                break
            elif(opt == 2):
                cantidad = -1*cantidad
                break
            else:
                print("Ingrese una opcion valida")
        print(f"Cantidad actualizada de {stockActual} a {stockActual + cantidad}")
        productos.get(codigo).update({"stock": (stockActual + cantidad)})
        pausa()
    else:
        print("No se encontro un producto con ese codigo")

def prodCriticos(productos : dict):
    productosCriticos =  dict()
    for key, item in productos.items():
        if ((item.get("stockMinimo")) > (item.get("stock"))):
            productosCriticos.update({key : item})
    print("Los productos criticos son los siguientes: ")
    verProd(productosCriticos)
    pausa()

def ganancia(productos : dict):
    borrarPantalla()
    gananciaTotal = 0
    formato = "{nombre:^20}|{ganancia:^20}"
    ganaciaPorProd = {}
    for item in productos.values():
        ganaciaProd = item.get("stock") * (item.get("valorVenta") - item.get("valorCompra"))
        ganaciaPorProd.update( {item.get("nombre") : {"nombre" : item.get("nombre"),"ganancia" : ganaciaProd}} )
        gananciaTotal += ganaciaProd
    print(formato.format(nombre = " Nombre Producto", ganancia = "Ganancia"))
    print("--------------------|--------------------")
    for item in ganaciaPorProd.values():
     print(formato.format(**item))

    print("\nLa ganancia total es de: ",gananciaTotal)
    pausa()

def comprobarDato (cadena, tipo):
    tipoUsuario = ""
    dato =""
    
    if(tipo == int):
        tipoUsuario = "entero"
    elif(tipo == float):
        tipoUsuario = "real"
    try:
        dato = tipo(input(f"{cadena}"))
    except ValueError:
        while(type(dato) != tipo):
            try:
                print(f"El dato debe ser de tipo {tipoUsuario}")
                dato = tipo(input(cadena))
            except ValueError:
                borrarPantalla()
        return dato
    else:
        return dato