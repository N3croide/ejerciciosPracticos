# Declaración de Variables
N = int(input("INGRESE DIMENSIÓN [MENOS O IGUAL A 20]: "))
M = [[0 for _ in range(21)] for _ in range(21)]  # Matriz de 20x20

# Crear el triángulo en la matriz
for IZQ in range(1, N + 1):
    for DER in range(1, N + 1):
        M[IZQ][DER] = 0

# Colocar el valor de 1 en los extremos
for IZQ in range(1, N + 1):
    M[IZQ][1] = 1

for DER in range(1, N + 1):
    M[DER][DER] = 1

# Calcular los valores internos del triángulo
for IZQ in range(3, N + 1):
    for DER in range(2, IZQ):
        M[IZQ][DER] = M[IZQ - 1][DER] + M[IZQ - 1][DER - 1]

# Mostrar el triángulo
for IZQ in range(1, N + 1):
    ESPACIOS = ""
    for _ in range(1, N - IZQ + 1):
        ESPACIOS += " "
    print(ESPACIOS, end="")
    for DER in range(1, IZQ + 1):
        VAL = M[IZQ][DER]
        print(VAL, end=" ")
    print("")
