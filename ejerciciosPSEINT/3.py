# Declaración de variables
total = 0
desc = 0

# Bucle para calcular el total de consumo
for cont in range(1, 11):  # De 1 a 10
    print("CONSUMO -", cont, ": $", end=" ")
    consumo = float(input())  # Lee el consumo ingresado por el usuario
    total += consumo

# Aplica descuento si el total es mayor a $50
if total > 50:
    desc = total * 0.07

# Muestra el consumo total, descuento y pago total
print("CONSUMO TOTAL : $", total)
print("DESCUENTO     : $", desc)
print("PAGO TOTAL    : $", total - desc)
