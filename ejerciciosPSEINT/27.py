print("INGRESE UN VALOR:")
num = int(input())
divisible = 0

for cont in range(2, num + 1):
    for divi in range(1, cont + 1):
        if cont % divi == 0:
            divisible += 1

    if divisible == 2:
        print(cont, end=" ")
    
    divisible = 0

print()
