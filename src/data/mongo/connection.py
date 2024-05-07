import pymongo
from pymongo.server_api import ServerApi

client = pymongo.MongoClient("mongodb+srv://root:root@fatec.e8bszzd.mongodb.net/?retryWrites=true&w=majority&appName=fatec", server_api=ServerApi('1'))
database = client.MercadoLivre
