from pydantic import computed_field
from pydantic_settings import BaseSettings
from typing import Literal


class Settings(BaseSettings):
    APP_NAME: str = "Awesome API"
    ADMIN_EMAIL: str = ""
    DB_USER: str = ""
    DB_PASSWORD: str = ""
    DB_HOST: str = ""
    DB_NAME: str = ""

    API_V1_STR: str = "/api/v1"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    ENVIRONMENT: Literal["local", "staging", "production"] = "local"

    @computed_field
    @property
    def server_start_config(self) -> dict:
        if self.ENVIRONMENT.lower() == "local":
            conf = {"app": "app:app", "host": "127.0.0.1", "port": 8000, "reload": True}
        else:
            conf = {"app": "app:app", "host": "0.0.0.0", "port": 8000, "reload": False}

        return conf

    class Config:
        # Replace this with the path to your .env file
        env_file = "template.env"


settings = Settings()

__all__ = ["settings"]
