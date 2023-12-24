def registrarDependencia(dependencias : dict):
    nombre = input("Ingrese el nombre de la Dependencia: ")
    produccionC02 = {
        "electricidad" : 0,
        "transporte" : 0,
        "dispositivos" : 0
    }
    if (nombre != ""):
        dependencias.update({nombre: produccionC02})
        print("{",nombre," : ",dependencias.get(nombre),"}")
    else:
        print("El nombre no puede estar vacio")


def buscarDependencia(dependencias :dict, nombre : str) -> dict:
    if (len(dependencias)):
        for key, item in dependencias.items():
            if key == nombre:
                return {key: item}
    else:
        print("No se encontro la dependencia")
        return None