import os
#Metodo para exclusivamente para comprobar que el numero sea positivo
def comprobarNum(numero) -> bool:
    if (numero > 0):
       return True
    else:
        return False
    
#Metodo que va a retornar el valor solo cuando el valor sea un numero entero positivo
def pedirNum() -> int:
    while(True):    
        try:
            numero = int(input("Ingrese un numero entero positivo: "))
        except ValueError:
            print("Porfavor ingrese un numero entero")
        else:
            if(comprobarNum(numero)):
                return numero
            else:
                os.system("cls")
                print("Tiene que ingresar un numero positivo, recuerde que el cero no es no positivo ni negativo.")


#MAIN FUNCTION
numero = 0
os.system("cls")
for i in range(0,3):
    numero += pedirNum()
print(numero)