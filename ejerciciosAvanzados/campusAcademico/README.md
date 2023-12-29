# Gestor de Seguimiento Académico para Campers de Programación

El programa ha sido diseñado para llevar el control académico de los campers inscritos en un programa intensivo de programación en CampusLands. Cumple con los siguientes requerimientos:

## Descripción del Proyecto

1. **Registro de Campers:**
   - Captura de información detallada de cada camper: ID, nombre, apellidos, dirección, acudiente, teléfonos y estado.

2. **Rutas de Entrenamiento:**
   - Ofrece opciones de rutas de formación: NodeJS, Java, NetCore.
   - Campers inscritos deben superar la prueba inicial para optar por una ruta.

3. **Registro y Evaluación:**
   - Posibilidad de registrar y evaluar notas de campers inscritos.
   - Aprobación si el promedio entre la nota teórica y práctica es >=60.

4. **Áreas de Entrenamiento:**
   - Tres áreas de entrenamiento con límite de 33 campers cada una.
   - Enseñanza de diferentes stacks tecnológicos dependiendo de la ruta.

5. **Creación de Rutas:**
   - Definición de nuevas rutas con áreas de aprendizaje específicas.

6. **Asignación a Rutas:**
   - Campers aprobados pueden ser asignados a rutas creadas.
   - Respeto de la capacidad máxima de cada área de entrenamiento.

7. **Entrenadores Asignados:**
   - Expertos dirigentes de cada ruta de entrenamiento.
   - Posibilidad de asignar múltiples rutas a un entrenador según su horario.

8. **Gestión de Matrículas:**
   - Módulo para asignar campers a rutas, expertos, fechas y salones de entrenamiento.

9. **Evaluaciones Periódicas:**
   - Evaluación mediante pruebas teóricas y prácticas.
   - Aprobación si el promedio es >=60, con pesos específicos para cada tipo de prueba.

10. **Rendimiento Estudiantil:**
    - Identificación de campers con bajo rendimiento.
    - Alertas y consulta de campers en riesgo.

11. **Módulo de Reportes:**
    - Listado de campers por estado, aprobados inicialmente, entrenadores activos, bajo rendimiento, asignados a rutas y detalle de aprobación por módulo.

## Tabla de Variables en Main

| Variable      | E/S  | Tipo de dato |
| ------------- | ---- | ------------ |
| campersNuevos | E/S  | Dict         |
| salones       | E/S  | Dict         |
| trainers      | E/S  | Lists        |
| db            | E/S  | Dict         |

### Main

Este módulo maneja el flujo del sistema y realiza llamadas a los distintos módulos del programa.

## Módulos

### campers

Maneja el registro y evaluación de los campers inscritos en el programa de programación.

**Funciones**:

- registrarCamper(campers: dict): Registra nuevos campers y su información detallada.
- buscarCamper(campers: dict, id: int): Busca un camper por ID y muestra su información si existe.
- matriculaCamers(db: dict, campersNuevos: dict, salones: dict): Gestiona la matrícula de campers aprobados.
- mostrarCampers(estado: str, campers: dict): Muestra campers según su estado (inscrito, aprobado, etc.).

### rutas

Maneja las operaciones relacionadas con las rutas de entrenamiento.

**Funciones**:

- registrarRuta(rutas: dict): Registra nuevas rutas y sus respectivos módulos.
- regTrainers(trainers: tuple, db: dict): Asigna entrenadores a rutas existentes.

### pruebas

Maneja las evaluaciones y pruebas a los campers.

**Funciones**:

- pruebasIniciales(campersNuevos: dict): Evalúa y actualiza el estado de los campers inscritos.
- pruebasModulos(db: dict): Realiza la evaluación de los campers por módulo y actualiza sus datos según los resultados.

### menus

Maneja los menús y la interacción con el usuario.

**Funciones**:

- seleccionMenu(opcionesValidas: list, optMenu: int) -> int: Muestra y permite seleccionar opciones del menú principal.
- seleccionCategoria() -> str: Muestra y permite seleccionar categorías para las operaciones del programa.

