suma = 0

print("INGRESE LA CANTIDAD DE NOTAS:")
n = int(input())

for cont in range(1, n + 1):
    print("NOTA", cont, ": ", end="")
    nota = float(input())
    suma += nota

promedio = suma / n
print("PROMEDIO:", promedio)
