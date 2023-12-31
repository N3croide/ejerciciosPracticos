# Entrada de Datos
llamada = int(input("CANTIDAD DE MINUTOS: "))

# Proceso
if llamada <= 5:
    costo = llamada * 0.9
else:
    costo = (5 * 0.9) + ((llamada - 5) * 1.1)

# Salida
print(f"EL COSTO ES: S/.{costo}")
