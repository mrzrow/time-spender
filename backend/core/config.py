import os

from pydantic import BaseModel
from dotenv import load_dotenv


load_dotenv()


class DatabaseSettings(BaseModel):
    url: str = os.environ.get('DB_PATH')
    echo: bool = bool(os.environ.get('DB_ECHO'))


class Settings(BaseModel):
    api_prefix: str = '/api'
    db: DatabaseSettings = DatabaseSettings()


settings = Settings()
