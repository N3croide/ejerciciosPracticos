H = int(input("Ingrese las horas: "))
M = int(input("Ingrese los minutos: "))
S = int(input("Ingrese los segundos: "))

costo = ((H * 3600) + (M * 60) + S) * 0.25

print("COSTO TOTAL:", costo)
