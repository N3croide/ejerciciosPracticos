num = int(input("Ingrese un número de 3 cifras: "))

cen = num // 100
res = num % 100
dec = res // 10
uni = res % 10

print("CENTENA:", cen)
print("DECENA:", dec)
print("UNIDAD:", uni)
