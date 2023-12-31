# Declaración de variables
frase = ""
a = 0
e = 0
i = 0
oo = 0
u = 0

# Ingreso de datos
print("FRASE: ")
frase = input()

# Proceso: Contar la cantidad de vocales
for cont in range(0, len(frase)):
    vocal = frase[cont].upper()

    if vocal == "A" or vocal == "Á":
        a += 1
    elif vocal == "E" or vocal == "É":
        e += 1
    elif vocal == "I" or vocal == "Í":
        i += 1
    elif vocal == "O" or vocal == "Ó":
        oo += 1
    elif vocal == "U" or vocal == "Ú":
        u += 1

# Salida de datos
print("CANTIDAD DE VOCALES:")
print("A:", a)
print("E:", e)
print("I:", i)
print("O:", oo)
print("U:", u)

