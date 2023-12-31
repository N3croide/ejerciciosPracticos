# Entrada de Datos
num = int(input("INGRESE NÚMERO DE 3 CÍFRAS: "))

# Proceso
c1 = num // 100
r1 = num % 100
c2 = (r1 - (r1 % 10)) // 10
r2 = r1 % 10

# Salida
if num == ((r2 * 100) + (c2 * 10) + c1):
    print("NÚMERO CAPICÚA")
else:
    print("NO ES CAPICÚA")
