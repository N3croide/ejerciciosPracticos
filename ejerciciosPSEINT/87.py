def decimal_a_romano(numero):
    romanos = {
        1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X',
        40: 'XL', 50: 'L', 90: 'XC', 100: 'C',
        400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'
    }
    resultado = ''
    valores = sorted(romanos.keys(), reverse=True)
    for val in valores:
        while numero >= val:
            resultado += romanos[val]
            numero -= val
    return resultado

# Ingreso de datos
numero = int(input("INGRESE NÚMERO: "))
# Mostrar el número en romanos
print(f"En Romanos: {decimal_a_romano(numero)}")
