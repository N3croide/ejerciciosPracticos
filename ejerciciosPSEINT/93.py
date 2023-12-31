# Ingreso de la letra
letra = input("Letra [V - P - C - J - F] : ")
letra = letra.upper()  # Convertir a mayúsculas

# Selección del lenguaje de programación
if letra == "V":
    print("Visual Basic")
elif letra == "P":
    print("Pascal")
elif letra == "C":
    print("C#")
elif letra == "J":
    print("Java")
elif letra == "F":
    print("Fortran")
else:
    print("Lenguaje no reconocido")
