import os

class Config:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Config, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def get_env_var(self, var_name, default_value=None):
        value = os.getenv(var_name)
        if value is None and default_value is not None:
            raise EnvironmentError(f"Environment variable {var_name} not found")
        else:
            value = default_value
        return value

    def get_env_var_list(self, var_name, default_value=None):
        value = self.get_env_var(var_name, default_value)
        return set(value.split(","))

    def get_storage_uri(self):
        mongo_connection_string = self.get_env_var("MONGO_CONNECTION_STRING")
        mongo_db_name = self.get_env_var("MONGO_DB_NAME")
        return f"{mongo_connection_string}/{mongo_db_name}"
