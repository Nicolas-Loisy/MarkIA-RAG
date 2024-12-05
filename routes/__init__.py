from flask import Blueprint
from .api import api_bp as api_routes_bp
from .chatbot import chatbot_bp
from .echo import echo_bp

api_bp = Blueprint('api', __name__)

@api_bp.before_request
def block_non_json():
    from flask import request
    from werkzeug.exceptions import BadRequest
    if request.accept_mimetypes['text/html'] > request.accept_mimetypes['application/json']:
        raise BadRequest("Only JSON responses are supported")

api_bp.register_blueprint(api_routes_bp, url_prefix='/')
api_bp.register_blueprint(chatbot_bp, url_prefix='/chatbot')
api_bp.register_blueprint(echo_bp, url_prefix='/echo')