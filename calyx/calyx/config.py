from pydantic import BaseModel
from dotenv import load_dotenv
import os

load_dotenv()

class EmbeddingConfig(BaseModel):
    """
    Embedding configuration
    """
    token:str = os.getenv("HF_TOKEN", "")
    model: str = os.getenv("MODEL_EMBEDDING")
    timeout_s:int = int(os.getenv("EMBEDDING_TIMEOUT_S", "180"))

class DBConfig(BaseModel):
    """
    DB Config (for inference)
    """
    db_name:str = os.getenv("DB_NAME", "movie_description.json")


class Settings(BaseModel):
    app_name: str = os.getenv("APP_NAME", "calyx")
    version: str = os.getenv("VERSION", "0.1.0")
    env: str = os.getenv("SERVICE_ENV", "local")
    token: str = os.getenv("TOKEN", "")
    request_timeout_s: int = int(os.getenv("REQUEST_TIMEOUT_S", "350"))

    embedding: EmbeddingConfig = EmbeddingConfig()
    db_config: DBConfig = DBConfig()

settings = Settings()