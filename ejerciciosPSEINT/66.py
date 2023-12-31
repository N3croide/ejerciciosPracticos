# Dibuja un triángulo según el carácter ingresado

# Ingreso de altura y carácter
alt = int(input("Altura del Triángulo: "))
caract = input("Ingrese un Carácter: ")

# Dibujo del triángulo
for i in range(1, alt + 1):
    # Mostrar los espacios vacíos
    for j in range(1, alt - i + 1):
        print(" ", end="")
    # Dibujar el triángulo con el carácter
    for j in range(1, i * 2):
        print(caract, end="")
    print()
