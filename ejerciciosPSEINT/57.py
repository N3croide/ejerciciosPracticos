dias = int(input("INGRESE CANTIDAD DE DÍAS: "))
A = dias // 365
M = (dias - (A * 365)) // 30
D = dias - ((A * 365) + (M * 30))

print("Año:", A)
print("Mes:", M)
print("Día:", D)
