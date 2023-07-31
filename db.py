import pymongo

cliente = pymongo.MongoClient('mongodb://localhost:27017')

db = cliente.proyecto_gracosoft

materias = db.materias