print("INGRESE NÚMERO:")
num = int(input())
divisi = 0

for divi in range(1, num + 1):
    if num % divi == 0:
        divisi += 1

if divisi == 2:
    print("NÚMERO PRIMO")
else:
    print("NO ES PRIMO")
