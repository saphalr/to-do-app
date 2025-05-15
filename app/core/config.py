from pydantic_settings import BaseSettings
from pydantic import ConfigDict


class Settings(BaseSettings):
    debug: bool = True
    environment: str
    port: int
    host: str
    db_user: str
    db_password: str
    db_name: str
    db_host: str
    db_port: str

    model_config = ConfigDict(env_file=".env")


settings = Settings()
