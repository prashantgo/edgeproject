from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_PORT: int
    POSTGRES_PASSWORD: str
    POSTGRES_USER: str
    POSTGRES_DB: str
    DATABASE_HOST: str
    DATABASE_HOSTNAME: str
    SOURCE_TABLE: str

    class Config:
        env_file = './.env'


settings = Settings()

