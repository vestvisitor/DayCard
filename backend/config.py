from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import computed_field
import os


class Settings(BaseSettings):
    DB_NAME: str
    DB_HOST: str
    DB_PORT : int

    API_URL: str
    API_TOKEN: str

    SECRET_KEY : str

    ACCESS_TOKEN_EXPIRE_MINUTES: int

    model_config = SettingsConfigDict(
        env_file=f"/{os.getcwd()}\\backend\\.env"
    )


Config = Settings()
