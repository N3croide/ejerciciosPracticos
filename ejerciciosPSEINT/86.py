# Ingreso de datos
dia = int(input("INGRESE DIA [1-7]: "))

# Verificación del día de la semana
if dia == 1:
    print("LUNES")
elif dia == 2:
    print("MARTES")
elif dia == 3:
    print("MIÉRCOLES")
elif dia == 4:
    print("JUEVES")
elif dia == 5:
    print("VIERNES")
elif dia == 6:
    print("SÁBADO")
elif dia == 7:
    print("DOMINGO")
else:
    print("Día Invalido")
