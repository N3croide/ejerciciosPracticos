sumaP = 0
sumaI = 0

print("INGRESE NÚMERO:")
num = int(input())

for x in range(1, num + 1):
    if x % 2 == 0:
        sumaP += x
    else:
        sumaI += x

print("Suma de Pares:", sumaP)
print("Suma de Impares:", sumaI)
