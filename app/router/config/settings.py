from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str
    DEBUG: bool = False
    DATABASE_URL: str
    SECRET_KEY: str
    PASSWORD:str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
