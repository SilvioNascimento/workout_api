from pydantic import Field
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DB_URL: str = Field(default='postgresql+asyncpg://postgres:admin123@localhost/workout')


settings = Settings()