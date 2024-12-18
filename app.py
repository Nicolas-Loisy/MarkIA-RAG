from flask import Flask
from flask_talisman import Talisman
from flask_cors import CORS
from utils.limiter import init_limiter
from utils.config import Config

config = Config()
app = Flask(__name__)

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

# Initialize limiter
init_limiter(app)

# Import and register blueprints at the end to avoid circular imports
from routes import api_bp

app.register_blueprint(api_bp, url_prefix='/api')

if __name__ == '__main__':
    # Utiliser HTTPS en production
    app.run(debug=True)
