
num = 0
val = 1
contador = 1
espacio = ''

print("MUESTRA GRÁFICA DE NÚMEROS COMO TRIÁNGULO.")
while num < 3:
    num = int(input("INGRESE NÚMERO: "))

print()

for x in range(1, num + 1):
    espacio = ''
    for z in range(1, num - x + 1):
        espacio += ' '
    print(espacio, end='')
    contador = 1
    for f in range(1, val + 1):
        print(contador, end='')
        if contador == 9:
            contador = 0
        else:
            contador += 1

    print()
    val += 2
