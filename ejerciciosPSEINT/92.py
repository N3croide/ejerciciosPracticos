# Tipos de seguro y sus costos
costos_seguro = {
    1: 45,
    2: 30,
    3: 15
}

# Ingreso del tipo de seguro
seguro = int(input("OPCIÓN : "))

# Cálculo del costo mensual
if seguro in costos_seguro:
    costo_mensual = costos_seguro[seguro]
    print("Pago Mensual: $", costo_mensual)
else:
    print("Error en el tipo de seguro.")
