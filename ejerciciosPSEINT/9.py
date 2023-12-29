# Bucle para generar la serie de asteriscos
XN = 7
for F in range(1, 8):  # De 1 a 7
    serie = ""
    if F >= 5:
        XN = XN + 2
    for C in range(1, XN - F + 1):  # De 1 a XN
        serie += "* "
    print(serie)
