# Ingreso de notas
N1 = float(input("Ingrese Nota 1: "))
N2 = float(input("Ingrese Nota 2: "))
N3 = float(input("Ingrese Nota 3: "))

# Cálculo del promedio
prom = round((N1 + N2 + N3) / 3)

# Mostrar nivel académico según el promedio
if 0 <= prom <= 10:
    print("NIVEL MALO")
elif 11 <= prom <= 13:
    print("NIVEL REGULAR")
elif 14 <= prom <= 16:
    print("NIVEL BUENO")
elif 17 <= prom <= 20:
    print("NIVEL MUY BUENO")
else:
    print("Valor de promedio incorrecto")
