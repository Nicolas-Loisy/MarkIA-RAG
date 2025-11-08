from flask import Blueprint, jsonify, request
from werkzeug.exceptions import BadRequest
from utils.limiter import limiter
from utils.security import require_api_key
from eurelis_llmatoolkit.llamaindex.config_loader import ConfigLoader
from eurelis_llmatoolkit.llamaindex.chatbot_wrapper import ChatbotWrapper

chatbot_bp = Blueprint('chatbot', __name__)

@chatbot_bp.route('/dumb', methods=['POST'])
@limiter.limit("10 per minute")
@require_api_key
def chatbot_dumb():
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
        "text": f"Je serai bientôt intelligent ! Vous avez dit : {user_message}"
    }
    return jsonify(response)


@chatbot_bp.route('/<chat_id>', methods=['POST'])
@limiter.limit("10 per minute")
@require_api_key
def chatbot(chat_id):
    # Vérifie si le contenu est bien en JSON
    if not request.is_json:
        raise BadRequest("Invalid content type. JSON required.")
    
    # Récupère les données JSON envoyées par le client
    data = request.json
    
    # Vérifie si le message de l'utilisateur est présent
    user_message = data.get("messages", [{}])[0].get("text")
    if not user_message:
        raise BadRequest("Missing 'text' in the 'messages' array.")
    
    try:
        # Chatbot configuration
        config_dict = ConfigLoader.load_config("llmatk.json")
        react_wrapper = ChatbotWrapper(config=config_dict, conversation_id=chat_id)
        answer = react_wrapper.run(user_message)
        # print(f"Chatbot answer: {str(answer)}")
        # Retourne le message de l'utilisateur dans une réponse JSON
        response = {
            "text": f"{str(answer)}"
        }

        return jsonify(response)
    except Exception as e:
        print(f"Error occurred: {str(e)}")
        raise BadRequest(f"An error occurred while processing the request !")