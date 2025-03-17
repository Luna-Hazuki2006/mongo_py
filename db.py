import pymongo
import os

cliente = pymongo.MongoClient(os.environ.get('URL'))

db = cliente.proyecto_gracosoft

materias = db.materias