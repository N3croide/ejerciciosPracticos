# Declaración de variables
xpro = 0
xnom = ""
promedio_mayor = 0

# Bucle para encontrar el alumno con el mayor promedio
for cont in range(1, 6):  # De 1 a 5
    print("NOMBRE:")
    nom = input()  # Lee el nombre del alumno
    print("PROMEDIO:")
    pro = float(input())  # Lee el promedio del alumno

    if xpro < pro:  # Compara el promedio con el máximo actual
        xpro = pro
        xnom = nom

# Muestra el alumno con el mayor promedio
print("ALUMNO CON MAYOR NOTA:", xnom)
print("PROMEDIO:", xpro)
