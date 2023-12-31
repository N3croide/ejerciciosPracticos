import random

# Valor de compra
compra = float(input("VALOR DE COMPRA : S/. "))

# Simulación de la elección de un color aleatorio
color = random.randint(1, 5)

# Inicializar descuento
desct = 0

# Mostrar el color sorteado y calcular el descuento correspondiente
if color == 1:
    print("COLOR: BLANCO")
    desct = 1
elif color == 2:
    print("COLOR: VERDE")
    desct = 0.5
elif color == 3:
    print("COLOR: NEGRO")
    desct = 0.4
elif color == 4:
    print("COLOR: CELESTE")
    desct = 0.05
else:
    print("COLOR: ROJO")
    desct = 0

# Calcular y mostrar el descuento, el importe descontado y el pago final
print(f"DESCUENTO: S/. {desct}")
importe_desct = compra * desct
print(f"IMPORTE DESCT.: S/. {importe_desct}")
pago_final = compra - importe_desct
print(f"PAGO FINAL: S/. {pago_final}")
