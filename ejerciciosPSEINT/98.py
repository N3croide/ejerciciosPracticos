# Declaración de variables
area = 0.0
base = 0.0
altura = 0.0

# Ingreso de Datos
print("MENU DE OPCIONES DE UN TRIÁNGULO")
print("1. Área de un triángulo, dada la base y la altura")
print("2. Base de un triángulo, dada la altura y el área")
print("3. Altura de un triángulo, dada la base y el área")
OPC = int(input("Selecciona una opción : "))

# Proceso
if OPC == 1:
    print("BASE : ")
    base = float(input())
    print("ALTURA: ")
    altura = float(input())
    area = (base * altura) / 2
    print("EL ÁREA ES : ", area)  # Salida
elif OPC == 2:
    print("ALTURA : ")
    altura = float(input())
    print("ÁREA : ")
    area = float(input())
    base = (area * 2) / altura
    print("LA BASE ES: ", base)  # Salida
elif OPC == 3:
    print("BASE : ")
    base = float(input())
    print("ÁREA : ")
    area = float(input())
    altura = (area * 2) / base
    print("LA ALTURA ES: ", altura)  # Salida
else:
    print("Error... Opción Incorrecta")  # Salida
