
costo = float(input("Costo de la Casa: S/. "))
iva = float(input("Valor del IVA (%): "))
print("")

iva_cantidad = costo * (iva / 100)
total_pagar = costo + iva_cantidad


print(f"IVA de {iva}%: S/. {iva_cantidad}")
print(f"Total a pagar: S/. {total_pagar}")
