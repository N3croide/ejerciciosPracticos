# Registro de Sismos en Ciudades

El Centro de Prevención de Sismos en Colombia necesita un programa para registrar y analizar sismos en 5 ciudades del país. Cada ciudad tendrá múltiples registros de sismos.

## Funcionalidades

El programa ofrece las siguientes opciones:

1. **Registrar Ciudad:** Permite agregar una ciudad al sistema.
2. **Registrar Sismo:** Registra los sismos en las ciudades.
3. **Buscar Sismos por Ciudad:** Permite buscar los sismos registrados para una ciudad específica.
4. **Informe de Riesgo:** Genera un informe de riesgo para cada ciudad según los sismos registrados.
5. **Salir:** Cierra el programa.

## Restricciones

1. **Igualdad en Registros:** Todas las ciudades deben tener la misma cantidad de sismos registrados.
2. **Clasificación de Riesgo:**
   - **Amarillo (Sin riesgo):** Promedio de sismos < 2.5
   - **Naranja (Riesgo medio):** Promedio de sismos entre 2.6 y 4.5
   - **Rojo (Riesgo alto):** Promedio de sismos > 4.5

## Tabla de Variables

| Variable | E/S                | Tipo    |
|:--------:|:----------------------------:|:-------:|
| optMenu  | **E** | int     |
| ciudades | **S**        | list    |



## Modulos



### Main

Este es el núcleo del programa, controla el flujo principal y utiliza las funciones de los otros módulos para interactuar con el usuario y gestionar los datos de las ciudades y los sismos.

- Defino funciones lambda para borrar la pantalla y hacer una pausa en la ejecución del programa.
- Inicia un bucle infinito (`while True`) para controlar el flujo principal del programa.
- Muestra un menú principal con cinco opciones y gestiona la selección del usuario.
- Ejecuta las operaciones correspondientes según la opción seleccionada:
  - Registrar Ciudad
  - Registrar Sismo
  - Buscar sismos por ciudad
  - Informe de riesgo
  - Salir





### Módulo menus

Este módulo se encarga de manejar las opciones del menú principal del programa.

#### Funciones y su funcionalidad:

1. menuPrincipal() -> int:

      - Muestra un menú con cinco opciones.

      - Permite al usuario seleccionar una opción.

      - Realiza validaciones para asegurar que la opción seleccionada esté en el rango de 1 a 5.

      - Retorna la opción seleccionada.



### Módulo ciudad

Este módulo maneja las operaciones relacionadas con las ciudades y los sismos registrados en ellas.

1. registrarSismo(ciudad: list) -> list:

      - Registra la magnitud de un sismo para una ciudad específica.

      - Utiliza excepciones para asegurar que la magnitud del sismo sea un valor numérico válido.

2. buscarSismo(ciudad: list):
   - Muestra la cantidad y magnitudes de sismos registrados para una ciudad.

3. informeSismos(ciudades: list)`:
   - Genera un informe de riesgo para cada ciudad basado en los promedios de los sismos registrados.



### Módulo sismos

Este módulo se encarga de gestionar los registros de sismos y generar informes de riesgo para cada ciudad.

#### Funciones y su funcionalidad:

1. registrarSismo(ciudad: list) -> list:

      - Registra la magnitud de un sismo para una ciudad específica.

      - Maneja excepciones para garantizar que la magnitud sea un valor numérico.

2. buscarSismo(ciudad: list):
   - Muestra la cantidad y magnitudes de sismos registrados para una ciudad.

3. informeSismos(ciudades: list):

   - Genera un informe de riesgo para cada ciudad basado en las magnitudes de los sismos.

   - Clasifica el riesgo como amarillo, naranja o rojo según los promedios de las magnitudes

     





