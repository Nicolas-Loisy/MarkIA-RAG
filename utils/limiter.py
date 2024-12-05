import os
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

# Charger les variables d’environnement
MONGO_CONNECTION_STRING = os.getenv("MONGO_CONNECTION_STRING")
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME")

# Construire l'URI pour Flask-Limiter
storage_uri = f"{MONGO_CONNECTION_STRING}/{MONGO_DB_NAME}"


limiter = Limiter(key_func=get_remote_address, storage_uri=storage_uri)

def init_limiter(app):
    limiter.init_app(app)