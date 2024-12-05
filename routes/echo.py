from flask import Blueprint, jsonify, request
from werkzeug.exceptions import BadRequest
from app import limiter
from utils.security import require_api_key

echo_bp = Blueprint('echo', __name__)

@echo_bp.route('/', methods=['POST'])
@limiter.limit("10 per minute")
@require_api_key
def echo():
    if not request.is_json:
        raise BadRequest("Invalid content type. JSON required.")
    data = request.json
    return jsonify({'you_sent': data})