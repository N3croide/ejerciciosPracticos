 # <center> IMC </center>

| VARIABLES  | E/S  | TIPO DE DATO |
| :--------: | :--: | :----------: |
|  isActive  | ---  |     bool     |
| estudiante | E/S  |     dict     |

La parte principal del programa lo usaremos para mostrar los datos requeridos(nombre, edad, imc, categoriaImc) y preguntaremos si quiere seguir ingresando mas estudiantes; el programa cuenta con 3 funciones;

1. verificarDato()

   Esta función la usaremos para verificar que los datos de la altura y el peso sean tipo float para realizar los cálculos del imc y retorna el dato.

2. calcularImc()

   En esta función vamos a pedir la altura y el peso ya que no la vamos a utilizar en ninguna otra parte del código, asi que usamos esos valores para calcular el imc y la categoría del imc y retornamos ambos valores como una lista.

3. ingresarEstudiante()

   En esta función vamos ingresar los datos que vamos a mostrar al usuario