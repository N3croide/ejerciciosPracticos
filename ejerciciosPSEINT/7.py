# Bucle para generar la secuencia y mostrar la gráfica
for F in range(1, 10):  # De 1 a 9
    s = 0
    serie = 0
    for C in range(1, 11 - F):  # De 1 a 10-F
        S = (10 - F)
        serie = (serie * 10) + S
    print(serie)
