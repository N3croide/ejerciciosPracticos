# Entrada de datos
cantidad = int(input("INGRESE CANTIDAD A COMPRAR: "))

# Proceso para obtener el costo a pagar
if cantidad in [1, 2, 3]:
    costo = 15
elif cantidad in [4, 5, 6, 7, 8]:
    costo = 11
else:
    costo = 10

# Salida de datos
print(f"COSTO POR TECLADO : S/. {costo}")
print(f"TOTAL A PAGAR : S/. {costo * cantidad}")
