from pydantic import BaseModel
from dotenv import load_dotenv
import os

load_dotenv()

class DBConfig(BaseModel):
    """
    DB Config
    """
    db_name:str = os.getenv("DB_NAME", "")
    db_path:str = os.getenv("DB_PATH", "") 

class LLMConfig(BaseModel):
    """
    LLM Configuration
    """
    api_key: str = os.getenv("GOOGLE_API_KEY", "")
    model: str = os.getenv("MODEL_NAME", "")
    model_provider: str = os.getenv("MODEL_PROVIDER", "")

class Settings(BaseModel):
    app_name: str = os.getenv("APP_NAME", "calyx")
    version: str = os.getenv("VERSION", "0.1.0")
    env: str = os.getenv("SERVICE_ENV", "local")

    db_config: DBConfig = DBConfig()
    llm_config: LLMConfig = LLMConfig()

settings = Settings()