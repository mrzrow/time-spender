from pydantic import BaseModel


class DatabaseSettings(BaseModel):
    url: str = 'sqlite+aiosqlite:///././db.sqlite'
    echo: bool = True


class Settings(BaseModel):
    api_prefix: str = '/api'
    db: DatabaseSettings = DatabaseSettings()


settings = Settings()
