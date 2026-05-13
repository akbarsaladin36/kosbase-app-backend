from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    database_host: str = 'localhost'
    database_port: int = 3306
    database_name: str
    database_username: str
    database_password: str
    jwt_secret_key: str
    jwt_algorithm: str
    jwt_access_expire_time: int
    mayar_base_url: str
    mayar_webhook_token: str
    mayar_api_key: str

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'

@lru_cache
def get_settings() -> Settings:
    return Settings()