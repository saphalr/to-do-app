from pydantic_settings import BaseSettings
from pydantic import ConfigDict


class Settings(BaseSettings):
    debug: bool = True
    environment: str = "development"
    port: int = 8000
    host: str = "127.0.0.1"
    secret_key: str

    model_config = ConfigDict(env_file=".env")


settings = Settings()
