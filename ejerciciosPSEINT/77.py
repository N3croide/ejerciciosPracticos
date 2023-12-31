# Entrada de Datos
nom = input("Ingrese Nombre: ")
sueldoB = float(input("Sueldo Básico: S/."))
hijos = int(input("Nro. de Hijos: "))

# Proceso
boni = 0
sueldoF = 0

if hijos > 0:
    boni = sueldoB * 0.7

sueldoF = sueldoB + boni

# Salida
print("\nBONIFICACIÓN: S/.", boni)
print("SUELDO FINAL: S/.", sueldoF)
