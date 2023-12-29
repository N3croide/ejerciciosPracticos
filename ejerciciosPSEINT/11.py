# Calcular el producto de N números
N = int(input("VALOR DE N: "))
pro = 1

for f in range(1, N + 1):  # De 1 a N
    print(f, end=" ")
    pro *= f

print("")
print("PRODUCTO DE", N, "ES", pro)
