# Declaración de Variables
r = 0
v = 0
a = 0
Mcolor = ""

N = int(input("CANTIDAD DE PERSONAS: "))

for i in range(1, N + 1):
    c = ""
    while c not in ["ROJO", "VERDE", "AZUL"]:
        c = input(f"PERSONA Nro. {i}\n[ROJO - VERDE - AZUL]: ").upper()
    
    if c == "ROJO":
        r += 1
    elif c == "VERDE":
        v += 1
    else:
        a += 1

if r > v and r > a:
    Mcolor = "ROJO"
elif v > r and v > a:
    Mcolor = "VERDE"
else:
    Mcolor = "AZUL"

print(f"CANTIDAD DE COLOR ROJO: {r}")
print(f"CANTIDAD DE COLOR VERDE: {v}")
print(f"CANTIDAD DE COLOR AZUL: {a}")
print(f"EL COLOR MAS ESCOGIDO ES: {Mcolor}")
