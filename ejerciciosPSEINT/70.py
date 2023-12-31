# Entrada de datos
n1 = int(input("INGRESE NOTA 01: "))
n2 = int(input("INGRESE NOTA 02: "))
n3 = int(input("INGRESE NOTA 03: "))

# Proceso
prom = (n1 + n2 + n3) / 3

# Salida
if prom > 10.5:
    print(f"APROBADO CON {prom}")
else:
    print(f"DESAPROBADO CON {prom}")
