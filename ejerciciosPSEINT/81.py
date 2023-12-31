# Entrada de datos
precio = float(input("INGRESE PRECIO: S/. "))
cant = int(input("INGRESE CANTIDAD: "))

# Inicialización de variables
IGV = 0
monto = 0

# Cálculo del monto y del IGV
print("05. CALCULAR IGV SEGUN EL MONTO DE COMPRA")
monto = precio * cant
if monto > 100:
    IGV = monto * 0.18  # 18%

# Salida de resultados
print("")
print(f"TOTAL : S/. {monto}")
print(f"IGV 18% : S/. {IGV}")
print(f"TOTAL A PAGAR : S/. {monto + IGV}")
