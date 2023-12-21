 # IMC
| VARIABLES  | E/S  | TIPO DE DATO |
| :--------: | :--: | :----------: |
|  contador  | E/S  |     dict     |
| estudiante | E/S  |     dict     |

La parte principal del programa lo usaremos para mostrar los datos requeridos(nombre, edad, imc, categoriaImc), se ingresaran 20 estudiantes y al final de los 20 mostraremos la estadisticas, el programa cuenta con 3 funciones;

1. verificarDato()

   Esta función la usaremos para verificar que los datos de la altura y el peso sean tipo float para realizar los cálculos del imc y retorna el dato.

2. calcularImc()

   En esta función vamos a pedir la altura y el peso ya que no la vamos a utilizar en ninguna otra parte del código, asi que usamos esos valores para calcular el imc y la categoría del imc y retornamos ambos valores como una lista y vamos a ir aumentando el contador de categoria de imc.

3. ingresarEstudiante()

   En esta función vamos ingresar los datos que vamos a mostrar al usuario y usaremos el resto de funciones que implementamos y al final va a retornar un diccionario llamado estudiante con los datos que necesitamos imprimir.