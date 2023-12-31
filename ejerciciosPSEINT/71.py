# Entrada de datos
num = int(input("INGRESE NÚMERO: "))

# Proceso
c = round(num / 2)
r = c % 2
re = num

# Salida
if re == 0:
    print("NÚMERO PAR")
else:
    print("NÚMERO IMPAR")
