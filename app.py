import os
from flask import Flask
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_talisman import Talisman
from flask_cors import CORS
from dotenv import load_dotenv

app = Flask(__name__)

# Load environment variables from a .env file if it exists
load_dotenv()

# Limitation par adresse IP
limiter = Limiter(get_remote_address, app=app, default_limits=["200 per day", "50 per hour"])

# Configuration des en-têtes de sécurité
csp = {
    'default-src': '\'none\'',  # Interdit tout contenu par défaut
    'connect-src': [
        '\'self\'',  # Autorise uniquement les requêtes AJAX/Fetch vers votre domaine
    ]
}
Talisman(
    app,
    content_security_policy=csp,
    strict_transport_security=True,  # Forcer HTTPS
    frame_options="DENY",  # Empêche l'API d'être embarquée dans un iframe
    x_content_type_options="nosniff",  # Bloque le MIME sniffing
    x_xss_protection=1  # Protection basique contre XSS
)

# Configuration des origines autorisées
origins = [
    "https://markia.fr",
    "https://markia.nicolasloisy.fr",
    "https://nicolasloisy.fr",
    "https://portfolio.nicolasloisy.fr"
]
CORS(app, resources={r"/api/*": {"origins": origins}}, methods=["GET", "POST"], supports_credentials=True)

from routes import api_bp

app.register_blueprint(api_bp, url_prefix='/api')

if __name__ == '__main__':
    # Utiliser HTTPS en production
    app.run(debug=True)
