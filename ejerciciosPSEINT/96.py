# Ingreso de la cantidad de teclados a comprar
cantidad = int(input("Cantidad a comprar: "))

# Cálculo del costo según la cantidad de teclados
if cantidad in [1, 2, 3]:
    costo = 15
elif cantidad in [4, 5, 6, 7, 8]:
    costo = 11
else:
    costo = 10

# Cálculo del total a pagar
total_pagar = costo * cantidad

# Mostrar el costo por teclado y el total a pagar
print(f"Costo por teclado: S/.{costo}")
print(f"Total a Pagar: S/.{total_pagar}")
