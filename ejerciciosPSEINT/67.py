# Dibujar un Rombo

# Ingreso de altura (número impar)
altura = int(input("Altura del rombo (número impar): "))
while altura % 2 != 1:
    altura = int(input("Por favor, ingrese un número impar para la altura: "))

# Parte superior del rombo
for i in range(1, altura + 1, 2):
    # Espacios vacíos
    for j in range((altura - i) // 2):
        print(" ", end="")
    # Parte superior del rombo
    for j in range(i):
        print("*", end="")
    print()

# Parte inferior del rombo
for i in range(altura - 2, 0, -2):
    # Espacios vacíos
    for j in range((altura - i) // 2):
        print(" ", end="")
    # Parte inferior del rombo
    for j in range(i):
        print("*", end="")
    print()
