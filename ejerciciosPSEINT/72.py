# Entrada de Datos
usuario = input("INGRESE USUARIO: ")
clave = int(input("INGRESE CLAVE: "))

# Proceso y Salida
if usuario == "ADMIN" and clave == 123456:
    print("ACCESO PERMITIDO")
else:
    print("ACCESO DENEGADO")
