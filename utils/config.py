import os
from dotenv import load_dotenv

class Config:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Config, cls).__new__(cls, *args, **kwargs)
            cls._load_env()
        return cls._instance

    @classmethod
    def _load_env(cls):
        load_dotenv()

    def get_env_var(self, var_name, default_value=None):
        value = os.getenv(var_name)
        if value is None:
            if default_value is not None:
                value = default_value
            else:
                raise EnvironmentError(f"Environment variable {var_name} not found")
        return value

    def get_env_var_list(self, var_name, default_value=None):
        value = self.get_env_var(var_name, default_value)
        return set(value.split(","))

    def get_storage_uri(self):
        mongo_connection_string = self.get_env_var("MONGO_CONNECTION_STRING")
        mongo_db_name = self.get_env_var("MONGO_DB_NAME")
        return f"{mongo_connection_string}/{mongo_db_name}"
