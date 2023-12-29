fact = 1

print("FACTORIAL A CALCULAR:")
num = int(input())

print("\nSERIE DEL FACTORIAL:", num)
for x in range(1, num + 1):
    print((num + 1) - x, end=" ")
    fact *= x

print("\n\nEL FACTORIAL ES:", fact)
