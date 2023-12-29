num = input("INGRESE NÚMERO: ")
tem = num[::-1]  # Invierte el número

print("")
print("NÚMERO INGRESADO:", num)
print("NÚMERO CAMBIADO:", tem)
print("")

if num == tem:
    print("SI ES UN NÚMERO CAPICÚA")
else:
    print("NO ES UN NÚMERO CAPICÚA")
