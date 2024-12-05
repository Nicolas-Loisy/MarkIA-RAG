
from flask import request
from werkzeug.exceptions import BadRequest

def block_non_json():
    if request.accept_mimetypes['text/html'] > request.accept_mimetypes['application/json']:
        raise BadRequest("Only JSON responses are supported")