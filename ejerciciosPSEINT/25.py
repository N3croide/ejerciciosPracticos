print("VALOR DE N:")
n = int(input())
suma = 1.0
d = 3

if n > 1:
    print(suma, end=" ")
    for i in range(2, n + 1):
        if i == n:
            print(f"{i}/{d}", end="")
        else:
            print(f"{i}/{d}", end=" + ")
        suma += i / d
        d += 2

print("\nLa suma es:", suma)
