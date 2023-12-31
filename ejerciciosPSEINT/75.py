monto = float(input("MONTO DE COMPRA: S/. "))

if monto >= 350:
    desct = monto * 0.35
    print(f"DESCUENTO ES DE 35% S/. {desct}")
else:
    desct = monto * 0.10
    print(f"DESCUENTO ES DE 10% = S/. {desct}")

print(f"MONTO A PAGAR: S/. {monto - desct}")
