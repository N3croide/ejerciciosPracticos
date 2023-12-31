# Ingreso de datos
num1 = int(input("NÚMERO 1: "))
num2 = int(input("NÚMERO 2: "))
operador = int(input("OPERADOR [1: +, 2: -, 3: x, 4: /]: "))

# Realizar operación
if operador == 1:
    print("SUMA:", (num1 + num2))
elif operador == 2:
    print("RESTA:", (num1 - num2))
elif operador == 3:
    print("MULTIPLICACIÓN:", (num1 * num2))
elif operador == 4:
    if num2 != 0:
        print("DIVISIÓN:", (num1 / num2))
    else:
        print("No se puede dividir por cero")
else:
    print("OPERADOR INCORRECTO")
