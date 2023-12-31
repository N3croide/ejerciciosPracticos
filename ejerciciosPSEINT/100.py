num = int(input("Ingrese número de hasta 2 cifras: "))

if 0 < num < 100:
    if 10 < num < 16:
        if num == 11:
            print("ONCE")
        elif num == 12:
            print("DOCE")
        elif num == 13:
            print("TRECE")
        elif num == 14:
            print("CATORCE")
        elif num == 15:
            print("QUINCE")
    else:
        DEC = (num // 10)
        UNI = (num % 10)
        DECENA = ""
        UNIDAD = ""
        
        if DEC == 1:
            DECENA = "DIECI"
        elif DEC == 2:
            DECENA = "VENTI"
        elif 2 < DEC < 10:
            if DEC == 3:
                DECENA = "TREINTA"
            elif DEC == 4:
                DECENA = "CUARENTA"
            elif DEC == 5:
                DECENA = "CINCUENTA"
            elif DEC == 6:
                DECENA = "SESENTA"
            elif DEC == 7:
                DECENA = "SETENTA"
            elif DEC == 8:
                DECENA = "OCHENTA"
            elif DEC == 9:
                DECENA = "NOVENTA"
        
        if UNI == 1:
            UNIDAD = "UNO"
        elif UNI == 2:
            UNIDAD = "DOS"
        elif UNI == 3:
            UNIDAD = "TRES"
        elif UNI == 4:
            UNIDAD = "CUATRO"
        elif UNI == 5:
            UNIDAD = "CINCO"
        elif UNI == 6:
            UNIDAD = "SEIS"
        elif UNI == 7:
            UNIDAD = "SIETE"
        elif UNI == 8:
            UNIDAD = "OCHO"
        elif UNI == 9:
            UNIDAD = "NUEVE"
        
        if UNI != 0:
            if DEC == 1 or DEC == 2:
                print(DECENA + UNIDAD)
            else:
                print(DECENA + " Y " + UNIDAD)
        else:
            print(DECENA)
else:
    print("Número Incorrecto...")
