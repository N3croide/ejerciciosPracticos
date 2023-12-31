# Declaración de Variables
refran = ""
C = 0
S = 0
D = 0
L = 0
R = 0
M = 0
consonante = 0

# Ingreso de Datos
print("Ingrese Refran:")
ref = input()

# Proceso: Eliminar los espacios en blanco del refran
for letra in ref:
    if letra != " ":
        refran += letra

# Proceso: Contar cuantas letras C, S, D, L, R y M hay
for letra in refran:
    letra = letra.upper()
    if letra == "C":
        C += 1
    if letra == "S":
        S += 1
    if letra == "D":
        D += 1
    if letra == "L":
        L += 1
    if letra == "R":
        R += 1
    if letra == "M":
        M += 1
    if letra not in ["A", "E", "I", "O", "U"] and letra.isalpha():
        consonante += 1

# Salida de Datos
print("CANTIDAD DE C:", C)
print("CANTIDAD DE S:", S)
print("CANTIDAD DE D:", D)
print("CANTIDAD DE L:", L)
print("CANTIDAD DE R:", R)
print("CANTIDAD DE M:", M)
print("CANTIDAD DE CONSONANTES:", consonante)
