# Declaración de Variables
ventas_hombres = 0
ventas_mujeres = 0
mujeres = 0

print("CANTIDAD DE EMPLEADOS:")
empleados = int(input())
print()

# Leer los datos de N empleados
for cont in range(1, empleados + 1):
    print("EMPLEADO Nro", cont, "/", empleados)
    nom = input("NOMBRE: ")
    genero = input("GÉNERO (H/M): ")
    ventas = float(input("VENTAS: "))
    print()

    # Obtener las ventas de hombres y mujeres
    if genero.upper() == "H":
        ventas_hombres += ventas
    else:
        ventas_mujeres += ventas
        mujeres += 1

# Salida de datos
print("TOTAL DE VENTAS HOMBRES:", ventas_hombres)
print("TOTAL DE VENTAS MUJERES:", ventas_mujeres)
print()
print("PORCENTAJE DE MUJERES:", (mujeres * 100) / empleados, "%")
