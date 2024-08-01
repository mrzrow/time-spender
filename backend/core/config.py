import os

from pathlib import Path
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()
BASE = Path(__file__).parent.parent


class DatabaseSettings(BaseModel):
    url: str = os.environ.get('DB_PATH').format(BASE)
    echo: bool = bool(os.environ.get('DB_ECHO'))


class Settings(BaseModel):
    api_prefix: str = '/api'
    db: DatabaseSettings = DatabaseSettings()


settings = Settings()
