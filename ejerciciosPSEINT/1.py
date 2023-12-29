# Entrada de datos
num = int(input("INGRESE NUMERO: "))

# Salida de datos - Mostrar tabla de multiplicar
for cont in range(1, 13):
    resultado = num * cont
    print(f"{num} x {cont} = {resultado}")
