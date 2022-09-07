from pydantic import BaseSettings, Field


class DatabaseSettings(BaseSettings):
    DB_URL: str


class SecuritySettings(BaseSettings):
    authjwt_secret_key: str = Field(env='SECRET_KEY')
