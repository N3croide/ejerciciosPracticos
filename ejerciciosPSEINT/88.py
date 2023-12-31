def obtener_estacion(numero):
    estaciones = {
        1: 'Verano',
        2: 'Otoño',
        3: 'Invierno',
        4: 'Primavera'
    }
    return estaciones.get(numero, 'Estación no válida')

# Ingreso de datos
numero = int(input("NÚMERO [1-4]: "))
# Mostrar la estación del año
print(obtener_estacion(numero))
