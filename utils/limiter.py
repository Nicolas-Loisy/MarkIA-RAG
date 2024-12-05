from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from .config import Config

config = Config()
limiter = Limiter(key_func=get_remote_address, storage_uri=config.get_storage_uri())

def init_limiter(app):
    limiter.init_app(app)