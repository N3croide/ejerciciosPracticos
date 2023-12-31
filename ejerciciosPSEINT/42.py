xseg = int(input("CANTIDAD DE SEGUNDOS: "))
hor = xseg // 3600
min = (xseg - (hor * 3600)) // 60
seg = xseg - (hor * 3600) - (min * 60)

print("HORAS:", hor)
print("MINUTOS:", min)
print("SEGUNDOS:", seg)
