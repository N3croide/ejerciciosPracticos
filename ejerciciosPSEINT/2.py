# Declaración de variables
par = 0
impar = 0

# Bucle para contar números pares e impares
for cont in range(1, 11):  # De 1 a 10
    print("NÚMERO", cont)
    num = int(input())  # Lee el número ingresado por el usuario

    if num % 2 == 0:  # Verifica si es par
        par += 1
    else:
        impar += 1

# Muestra la cantidad de pares e impares
print("CANTIDAD DE PARES:", par)
print("CANTIDAD DE IMPARES:", impar)
