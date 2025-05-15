from pydantic_settings import BaseSettings
from pydantic import ConfigDict


class Settings(BaseSettings):
    debug: bool = True
    environment: str = "development"
    port: int = 8000
    host: str = "0.0.0.0"
    db_user: str = "postgres"
    db_password: str = "postgres"
    db_name: str = "todos"
    db_host: str = "localhost"
    db_port: str = "5432"

    model_config = ConfigDict(env_file=".env")


settings = Settings()
