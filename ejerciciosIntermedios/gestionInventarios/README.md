## Tabla de Variables en Main

| Variable  | E/S  | Tipo de dato |
| --------- | ---- | ------------ |
| productos | E/S  | Dict         |


## Main
- Controla el flujo principal del programa, mostrando el menú y gestionando las operaciones del inventario según la selección del usuario. Utiliza un diccionario para almacenar los productos.

## Módulo inventarios

- seleccionMenu() -> int:

  - Muestra un menú interactivo con opciones para el usuario.

  - Permite seleccionar una opción del menú y retorna la opción elegida como un entero.

    

- registrarProd(producto: dict) -> dict: 

  - Registra un nuevo producto en el inventario solicitando al usuario ingresar detalles como código, nombre, valores de compra y venta, límites de stock, proveedor y cantidad.

  - Agrega el producto registrado al diccionario de productos y devuelve el diccionario actualizado.

    

- verProd(prods: dict): Muestra una tabla detallada con la información de los productos registrados.

  - Presenta una tabla detallada con información de todos los productos registrados.

  - Muestra en formato tabular los códigos, nombres, cantidades, valores de compra y venta, límites de stock y proveedores de cada producto.

  - Presenta una tabla detallada con información de todos los productos registrados.

  - Muestra en formato tabular los códigos, nombres, cantidades, valores de compra y venta, límites de stock y proveedores de cada producto.

    

- actualizacionStock(productos: dict): Actualiza el stock de un producto específico.

  - Facilita la actualización del stock de un producto específico.

  - Permite al usuario seleccionar un producto por su código y realizar cambios en el stock (agregar o restar cantidad).

  - Actualiza el valor del stock del producto en el diccionario de productos.

    

- prodCriticos(productos: dict): Identifica y muestra productos con stock por debajo del límite mínimo.

  - Identifica y muestra los productos cuyo stock está por debajo del límite mínimo establecido.

  - Presenta una tabla detallada con información de los productos que tienen un stock inferior al límite mínimo definido.

    

- ganancia(productos: dict): Calcula la ganancia potencial para cada producto y la ganancia total.

  - Calcula la ganancia potencial para cada producto en base al stock, valor de compra y valor de venta.
  - Muestra una tabla con la ganancia de cada producto y la ganancia total de todo el inventario.