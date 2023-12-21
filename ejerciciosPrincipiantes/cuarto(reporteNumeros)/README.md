# 	REPORTE N NUMEROS INGRESADOS

|   VARIABLES    | E/S  | TIPO DE DATO |
| :------------: | :--: | :----------: |
|    isActive    |  --  |     Bool     |
|     numero     |  E   |     Int      |
|  totalNumeros  |  --  |     List     |
| reporteNumeros |  S   |     Dict     |

En la parte principal del programa se llama a la funcion que nos permite ingresar el valor y comprueba a la vez si es valido, comparamos si es positivo o negativo para imprimir o seguir ingresando numeros, hay dos funciones principales:

1. verificarNumero:

   Sera la funcion encargada de pedir el numero y asegurarse de que el numero ingresado sea un entero

2. actualizarReporte:

   Esta funcion es donde se actualizara el diccionario de reportes, se usan funciones lambda para evitar hacer if por cada punto del reporte que toca imprimir, luego se hacen unas comprobaciones para ver si es posible agregar ese dato, es para evitar hacer divisiones por cero y comprobar si un numero es par