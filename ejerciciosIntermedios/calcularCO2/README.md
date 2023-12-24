


|   Variable   | E/S | Tipo |
| :----------: | :-----: | :--: |
| dependencias |    S    | dict |
|   optMenu    |    E    | int  |


## Modulos

### Main

- Inicia un bucle infinito para manejar las opciones del menú.
- Muestra un menú principal y permite al usuario seleccionar una opción.
- Ejecuta operaciones dependiendo de la opción seleccionada:
  - Registrar Dependencia
  - Registrar Consumo por Dependencia
  - Ver CO2 producido
  - Dependencia que produce mayor CO2
  - Salir del programa

### Módulo c02

- registrarConsumo (dependencias: dict):
   - Registra el consumo de dispositivos, transporte y electricidad para una dependencia específica.
   - Calcula las emisiones de CO2 según los datos ingresados.
   - Actualiza los datos de emisiones de la dependencia.

- mostrarCO2 (dependencias: dict):
   - Muestra el consumo de CO2 de cada dependencia y el total de CO2 producido.

- mayoCO2 (dependencias: dict):
   - Identifica la dependencia que produce la mayor cantidad de CO2.

- comprobarDato (dato, tipo):
   - Verifica y convierte el tipo de dato ingresado por el usuario.

### Módulo menus

- mostrarMenu() -> int:
   - Muestra el menú principal y permite al usuario seleccionar una opción.
   - Valida la entrada del usuario para asegurar una selección válida.

- mostrarMenuConsumo() -> int:
   - Muestra el menú para registrar el consumo por tipo (dispositivos, transporte, electricidad).
   - Valida la entrada del usuario para asegurar una selección válida.

### Módulo dependencias

- registrarDependencia (dependencias: dict):
   - Registra una nueva dependencia y sus emisiones de CO2 iniciales.

- buscarDependencia (dependencias: dict, nombre: str) -> dict:
   - Busca una dependencia por su nombre y devuelve su información.

