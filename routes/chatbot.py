from flask import Blueprint, jsonify, request
from werkzeug.exceptions import BadRequest
from utils.limiter import limiter
from utils.security import require_api_key

chatbot_bp = Blueprint('chatbot', __name__)

@chatbot_bp.route('/', methods=['POST'])
@limiter.limit("10 per minute")
@require_api_key
def chatbot():
    # Vérifie si le contenu est bien en JSON
    if not request.is_json:
        raise BadRequest("Invalid content type. JSON required.")
    
    # Récupère les données JSON envoyées par le client
    data = request.json
    
    # Vérifie si le message de l'utilisateur est présent
    user_message = data.get("messages", [{}])[0].get("text")
    if not user_message:
        raise BadRequest("Missing 'text' in the 'messages' array.")
    
    # Retourne le message de l'utilisateur dans une réponse JSON
    response = {
        "text": f"Je serais bientôt intelligent ! Vous avez dit : {user_message}"
    }
    return jsonify(response)