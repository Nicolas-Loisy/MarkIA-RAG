from flask import Blueprint
from .api import api_bp as api_routes_bp
from .chatbot import chatbot_bp
from .echo import echo_bp
from utils.block_non_json import block_non_json

api_bp = Blueprint('api', __name__)

api_bp.before_request(block_non_json)

api_bp.register_blueprint(api_routes_bp, url_prefix='/')
api_bp.register_blueprint(chatbot_bp, url_prefix='/chatbot')
api_bp.register_blueprint(echo_bp, url_prefix='/echo')