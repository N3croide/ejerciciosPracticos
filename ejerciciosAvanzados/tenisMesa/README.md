El programa hará de de ayuda en un torneo de tenis de mesa, los requisitos son los siguientes: 

1. El departamento de bienestar de campus desea organizar un torneo de tenis de mesa y requiere
Un programa que le permita llevar el control de los juegos llevados a cabo por cada uno de los
Inscritos en el torneo. El programa debe cumplir con los siguientes requerimientos:
1. Se tienen 3 categorías (Novato, Intermedio y Avanzado)
2. Cada partido ganado representa 2 puntos para el ganador.
3. Puntos a favor. Los puntos a favor se calculan con los puntos realizados en el juegos restando lo puntos
Recibidos en contra. Ej. Si en el set uno gano 11-7 tiene 4 puntos a favor.
4. El programa debe permitir registrar a cada jugador por categoría.
5. Cada categoría debe tener un mínimo de 5 inscritos para iniciar los juegos en la categoría.
6. En la categoría novatos solo se permiten jugadores entre 15 y 16 años, en intermedio jugadores entre
17 y 20 años y Avanzado jugadores mayores a 20 años.
7. El programa debe permitir llevar un registro detallado de cada jugador. Por ejemplo:

Id 	Jugador 	PJ    PG  PP PA TP
125	 Abc		 1   1      0    5   2

8. El programa debe permitir conoce el ganador por categoría. En caso de existir un empate el ganador será
El que tenga mas PA(Punto a favor)

## Tabla de Variables en Main

| Variable  | E/S  | Tipo de dato |
| --------- | ---- | ------------ |
| jugadores | E/S  | Dict         |
| ganadores | E/S  | Dict         |

### Main

Es el encargado del flujo del sistema y el encargado de hacer llamado a los modulos.

## Modulos

### torneo

Este módulo maneja las operaciones relacionadas con el torneo de tenis de mesa, incluyendo el registro de jugadores, el inicio de los juegos y la determinación de ganadores.

**Funciones**:

- registrarJugador(jugadores : dict): Registra nuevos jugadores en sus respectivas categorías y asigna puntajes iniciales.

- iniciarJuego(categoria : str, jugadores : dict, ganadores : dict): Inicia los juegos entre los jugadores de una categoría y registra los puntajes.
- ganador(categoria : str, jugadores : dict, ganadorCat : dict): Determina al ganador de una categoría y actualiza los datos de los ganadores.
- comprobarDato (cadena, tipo): Valida los datos ingresados por el usuario.

### menus

Se encarga de la presentación de los menús y la interacción con el usuario.

**Funciones**:

- seleccionMenu() -> int: Muestra el menú principal y permite seleccionar una opción.
- seleccionCategoria() -> str: Muestra el menú de categorías y permite seleccionar una para las operaciones del torneo.