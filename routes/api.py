from flask import Blueprint, jsonify
from utils.limiter import limiter
from utils.security import require_api_key

api_bp = Blueprint('api', __name__)

@api_bp.route('/', methods=['GET'])
@limiter.limit("10 per minute")
@require_api_key
def hello_world():
    return jsonify({'message': 'Hello, MarkIA RAG!'})