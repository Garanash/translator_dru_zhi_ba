from pydantic import BaseSettings


class Settings(BaseSettings):
    app_title: str = 'FastAPI app'
    description: str = 'It was lot of fun'
    database_url: str = 'sqlite+aiosqlite:///./fastapi.db'
    secret: str = 'SECRET'

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


settings = Settings()
