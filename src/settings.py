from pydantic_settings import BaseSettings
from pydantic import SecretStr


class Settings(BaseSettings):
    model_config = {
        "env_file": ".env", 
        "env_file_encoding": "utf-8",
        "extra": "ignore",  # Ignore unexpected environment variables
    }

    AZURE_API_KEY: SecretStr
    AZURE_API_BASE: str
    AZURE_API_VERSION: str

    # OPENAI_API_KEY: str

    LLM_DEPLOYMENT_NAME: str
    EMBEDDING_DEPLOYMENT_NAME: str

    SERPER_API_KEY: SecretStr

    MLFLOW_TRACKING_URI: str


settings = Settings()


llm_settings = {
    "provider": "azure_openai",
    "config": {
        "base_url": settings.AZURE_API_BASE,
        "api_version": settings.AZURE_API_VERSION,
        "api_key": settings.AZURE_API_KEY.get_secret_value(),
        "model": settings.LLM_DEPLOYMENT_NAME,
    },
}

embedder_settings = {
    "provider": "openai",
    "config": {
        "api_key": settings.AZURE_API_KEY.get_secret_value(),
        "api_base": settings.AZURE_API_BASE,
        "model": settings.EMBEDDING_DEPLOYMENT_NAME,
    },
}
