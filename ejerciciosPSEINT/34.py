# Declaración de variables
tarifa = 0.0
bus = 0
van = 0
micro = 0
man = 0
noc = 0

# Ingreso de datos
print("GANANCIAS DE UNA GARITA DE CONTROL")
print()
cantidad = int(input("CANTIDAD DE VEHÍCULOS: "))

# Proceso: Calcula la tarifa según el vehículo
for cont in range(1, cantidad + 1):
    print(f">> TIPO DE VEHÍCULO Nro {cont}/{cantidad}:")
    print("1. Ómnibus.")
    print("2. Minivan.")
    print("3. Micro.")
    tipo = int(input("OPCIÓN: "))

    if tipo == 1:
        tarifa = 13
        bus += tarifa
    elif tipo == 2:
        tarifa = 10
        van += tarifa
    elif tipo == 3:
        tarifa = 8
        micro += tarifa

    turno = input("TURNO (M/N): ")
    if turno.upper() == "M":
        man += tarifa
    else:
        noc += tarifa
    print()

# Salida de datos
print("IMPORTE DE TURNO MAÑANA:", man)
print("IMPORTE DE TURNO NOCHE:", noc)
print("IMPORTE DE ÓMNIBUS:", bus)
print("IMPORTE DE MINIVAN:", van)
print("IMPORTE DE MICRO:", micro)
