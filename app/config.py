from enum import Enum

from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv()


class Permissions(str, Enum):
    FAVORITES_WRITE = "favorites.own:write"
    FAVORITES_READ = "favorites.own:read"
    FAVORITES_DELETE = "favorites.own:delete"
    FAVORITES_OWN_FULL = "favorites.own:full"

    FAVORITES_READ_ALL = "favorites.all:read"


class Environment(str, Enum):
    DEVELOPMENT = "development"
    PRODUCTION = "production"

class Settings(BaseSettings):
    #Application
    APP_NAME: str = "favorites-service"
    DEBUG: bool = True
    ROOT_PATH: str = ''
    ENVIRONMENT: Environment = Environment.DEVELOPMENT

    @property
    def enable_docs(self) -> bool:
        return self.ENVIRONMENT in [Environment.DEVELOPMENT]

    # Database
    DB_HOST: str = "localhost"
    DB_PORT: str = "5432"
    DB_NAME: str = "test_db"
    DB_USER: str = "postgres"
    DB_PASS: str = "testpass"

    #Redis
    REDIS_URL: str = "redis://localhost:6379"

    #rpc
    RPC_API_URL: str = "localhost:50051"

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

settings = Settings()