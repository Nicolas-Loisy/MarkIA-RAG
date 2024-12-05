from flask import Flask, jsonify, request
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_talisman import Talisman
from flask_cors import CORS
from werkzeug.exceptions import BadRequest

app = Flask(__name__)

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

@app.before_request
def block_non_json():
    if request.accept_mimetypes['text/html'] > request.accept_mimetypes['application/json']:
        raise BadRequest("Only JSON responses are supported")

# Exemple d'endpoint
@app.route('/api', methods=['GET'])
@limiter.limit("10 per minute")
def hello_world():
    return jsonify({'message': 'Hello, Firebase!'})

# Endpoint avec un paramètre
@app.route('/api/echo', methods=['POST'])
@limiter.limit("10 per minute")
def echo():
    if not request.is_json:
        raise BadRequest("Invalid content type. JSON required.")
    data = request.json
    return jsonify({'you_sent': data})

if __name__ == '__main__':
    # Utiliser HTTPS en production
    app.run(debug=True)
