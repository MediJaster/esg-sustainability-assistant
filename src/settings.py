"""Application settings and model provider configuration.

This module sources configuration from environment variables via
``pydantic-settings`` and exposes ready-to-use dictionaries for LLM and
embedding providers.
"""

import os

from pydantic_settings import BaseSettings
from pydantic import SecretStr

OUTPUT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "out"))


class Settings(BaseSettings):
    """
    Typed settings loaded from ``.env`` and environment.

    Attributes
    ----------
    AZURE_API_KEY : SecretStr
        Azure OpenAI API key.
    AZURE_API_BASE : str
        Azure OpenAI base URL.
    AZURE_API_VERSION : str
        Azure OpenAI API version.
    LLM_DEPLOYMENT_NAME : str
        Deployment name for the chat/completion model.
    EMBEDDING_DEPLOYMENT_NAME : str
        Deployment name for the embedding model.
    SERPER_API_KEY : SecretStr
        Serper.dev API key for web search.
    MLFLOW_TRACKING_URI : str
        MLflow tracking server URI.
    """
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
