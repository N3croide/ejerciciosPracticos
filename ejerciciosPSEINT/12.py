# Números del rango de menor a mayor
A = int(input("NÚMERO A: "))
B = int(input("NÚMERO B: "))

if A < B:
    for N in range(A + 1, B):
        print(N)
else:
    for N in range(B + 1, A):
        print(N)
