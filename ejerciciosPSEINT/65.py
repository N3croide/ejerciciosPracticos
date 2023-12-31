
import math

r = float(input("RADIO: "))
h = float(input("ALTURA: "))

a = 2 * math.pi * r * (h + r)
v = math.pi * (r ** 2) * h

print("ÁREA TOTAL DEL CILINDRO:", a, "cm2")
print("VOLUMEN DEL CILINDRO:", v, "cm3")
