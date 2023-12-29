import random

sw = 0
numA = random.randint(1, 20)

for i in range(1, 4):
    print("ENCUENTRE EL NÚMERO [1 - 20] = ")
    num = int(input())
    
    if num == numA:
        print("NÚMERO ENCONTRADO")
        sw = 1
        break
    else:
        if num > numA:
            print("INGRESE UN NÚMERO MENOR")
        else:
            print("INGRESE UN NÚMERO MAYOR")
    
    print()

if sw == 0:
    print("EL NÚMERO A ENCONTRAR ERA:", numA)
