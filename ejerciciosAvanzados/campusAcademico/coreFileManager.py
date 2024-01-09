import json, os

RUTA_DB  ='ejerciciosAvanzados/campusAcademico/data/datos.json'

# def delete(*args):
#     data = (args)
#     data[0].update({data[1] : data[2]})
#     createFile(data[0])

def createFile(*args):
    with open(RUTA_DB,'w') as db:
        json.dump(args[0], db, indent=2)

def updateFile(*args):
    data = readFile()
    with open(RUTA_DB, 'w') as db:
        data[args[0]] = args[1]
        json.dump(data, db, indent = 3)

def readFile():
    with open(RUTA_DB,"r") as db:
        return json.load(db)

def checkFile(*args):
    data = list(args)
    if (os.path.isfile(RUTA_DB)):
        if(len(args) > 0):
            data[0] = readFile()
        print("Base de datos cargada...")
        os.system('pause')
    else:
        createFile(data[0])

#0 = rutas, 1 = campersNuevos, 2 = trainers, 3 = salones
def loadFile(*args):
    argsTemp = list(args)
    data = readFile()
    for i, item in enumerate(args):
        argsTemp[i] = data.get( (list(data.keys())[i]) )
    return argsTemp
