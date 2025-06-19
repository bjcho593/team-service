from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Cargar variables desde .env
load_dotenv()

# Obtener variables de entorno
MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017")
MONGO_DB = os.getenv("MONGO_DB", "teamsdb")

# Crear cliente de MongoDB
client = MongoClient(MONGO_URL)

# Seleccionar la base de datos
db = client[MONGO_DB]

# Colección de equipos
team_collection = db["teams"]
