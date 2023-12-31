# Declaración de variables
edad = 0
diax = 21
mesx = 10
aniox = 2023

# Registra 10 niños
for x in range(1, 11):
    print("DNI: ")
    dni = input()
    print("DÍA DE NACIMIENTO: ")
    dia = int(input())
    print("MES DE NACIMIENTO: ")
    mes = int(input())
    print("AÑO DE NACIMIENTO: ")
    anio = int(input())
    print("GÉNERO (H/M): ")
    genero = input()

    print("FECHA ACTUAL:", diax, "/", mesx, "/", aniox)
    edad = aniox - anio

    if mes > mesx:
        edad -= 1
    elif mes == mesx and dia > diax:
        edad -= 1

    print("EDAD:", edad, "años")

    if edad >= 8:
        print("RECIBE TABLET")
    elif edad == 6:
        if genero == "H":
            print("RECIBE CARRITO")
        else:
            print("RECIBE MUÑECA")

    print()

print()
