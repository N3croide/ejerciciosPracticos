def registrarDependencia() -> dict:
    nombre = input("Ingrese el nobmre de la Dependencia: ")
    produccionC02 = {
        "electricidad" : 0,
        "transporte" : 0,
        "dispossitivos" : 0
    }
    return {nombre: produccionC02}

def buscarDependencia(dependencias :dict, nombre : str) -> dict:
    for key, item in dependencias.items():
        if key == nombre:
            return {key: item}