# Claves y costos
tarifas = {
    1: 0.13,
    2: 0.11,
    5: 0.52,
    6: 0.99,
    8: 0.17,
    9: 0.17,
    10: 0.20,
    15: 0.59,
    20: 0.28
}

# Entrada de datos
clave = int(input("INGRESE CLAVE DESTINO: "))
minutos = int(input("DURACIÓN DE LA LLAMADA (minutos): "))

# Cálculo de costo
if clave in tarifas:
    costo = minutos * tarifas[clave]
    print("COSTO: $", costo)
else:
    print("!! Error en clave !!")
