monto = 1000.0
intereses = 0.0
total_pagar = 0.0

meses = int(input("Número de meses: "))

intereses = monto * (meses * 0.02)
total_pagar = monto + intereses

print("INTERESES:", intereses)
print("TOTAL A PAGAR:", total_pagar)
