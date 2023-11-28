from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    DB_US: str = Field(default='', env='DB_US')
    DB_PASS: str = Field(default='', env='DB_PASS')
    DB_HOST: str = Field(default='', env='DB_HOST')
    DB_NAME: str = Field(default='', env='DB_NAME')

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'
        case_sensitive = True

settings = Settings()