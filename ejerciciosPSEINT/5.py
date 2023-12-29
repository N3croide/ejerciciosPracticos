# Declaración e inicialización de variables
A = 0
B = 1
C = 0

# Bucle para generar la serie de Fibonacci y mostrar los primeros 10 números
for cont in range(1, 11):  # De 1 a 10
    print(C, end=" ")
    A, B = B, C
    C = A + B
