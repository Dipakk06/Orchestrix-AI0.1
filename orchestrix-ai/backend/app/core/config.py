from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Orchestrix AI"
    app_env: str = "development"
    secret_key: str = "super-secret-change-me"
    jwt_algorithm: str = "HS256"
    jwt_expire_minutes: int = 60 * 24

    postgres_url: str = "postgresql+psycopg://postgres:postgres@localhost:5432/orchestrix"
    chroma_host: str = "localhost"
    chroma_port: int = 8001

    ollama_base_url: str = "http://localhost:11434"
    ollama_model: str = "gemma3"

    whisper_model: str = "base"
    tts_engine: str = "pyttsx3"

    cors_origins: str = "http://localhost:3000"

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")


@lru_cache
def get_settings() -> Settings:
    return Settings()
