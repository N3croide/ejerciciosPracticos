# Entrada de datos
venta = float(input("INGRESE MONTO DE VENTA : $. "))

# Cálculo de bonificación
print("84. CALCULAR BONIFICACIÓN")
print("")
if venta > 2000:
    print(f"BONIFICACIÓN 10 %: $ {venta * 0.10}")
else:
    print(f"BONIFICACIÓN 50%: $ {venta * 0.50}")
