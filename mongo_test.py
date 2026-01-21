from pymongo import MongoClient

# Connexion MongoDB (conteneur Docker)
MONGO_URI = "mongodb://root:rootpass@localhost:27017/admin"

client = MongoClient(MONGO_URI)

# Accès à la base
db = client["medicaldb"]

print("Connexion MongoDB réussie")
print("Bases disponibles :", client.list_database_names())
