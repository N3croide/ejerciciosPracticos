
ope = ''
sumatoria = 0.0
v = 4.0
v1 = 5.0
v2 = 1.0
x = 2.0
x1 = 0.5

print("MUESTRA SERIE DE NÚMEROS")
print()
n = int(input("VALOR DE N: "))

for i in range(1, n + 1):
        
    if i != n:
        print(v, "/", x, ope, end=' ')
    else:
        print(v, "/", x, end='...')

    if (i % 2) == 1:
        ope = "+"
        sumatoria += (v / x)
    else:
        ope = "-"
        sumatoria -= (v / x)


    v += v1
    v1 += v2
    v2 += 1
    x *= x1
    x1 += x1

print("\n")
print("SUMATORIA:", sumatoria)
