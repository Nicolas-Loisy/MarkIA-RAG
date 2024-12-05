import os
from flask import request, jsonify
from functools import wraps
from .config import Config

config = Config()

API_KEYS = config.get_env_var_list("MARIKIA_API_KEYS")

def require_api_key(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        api_key = request.headers.get('x-api-key')
        if api_key not in API_KEYS:
            return jsonify({"message": "Forbidden"}), 403
        return f(*args, **kwargs)
    return decorated_function