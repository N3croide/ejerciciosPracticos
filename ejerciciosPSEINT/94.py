# Ingreso de datos
sueldo = float(input("Sueldo Base : S/."))
categoria = int(input("Categoría: 1.A - 2.B - 3.C - 4.D: "))

# Cálculo de bonificación según la categoría
if categoria == 1:
    bonificacion = sueldo * 0.1  # 10%
elif categoria == 2:
    bonificacion = sueldo * 0.2  # 20%
elif categoria == 3:
    bonificacion = sueldo * 0.3  # 30%
elif categoria == 4:
    bonificacion = sueldo * 0.5  # 50%
else:
    print("Categoría inválida")
    exit()

# Resultados
print("BONIFICACIÓN: S/.", bonificacion)
print("SUELDO NETO: S/.", sueldo + bonificacion)
