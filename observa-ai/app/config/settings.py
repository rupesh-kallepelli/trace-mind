from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional


class Settings(BaseSettings):
    """
    Centralized application configuration using environment variables.
    Supports OpenSearch, Vertex AI, and OpenAI LLM providers.
    """

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    # =========================
    # ✅ OpenSearch Settings
    # =========================
    OPENSEARCH_HOST: str = "localhost"
    OPENSEARCH_PORT: int = 9200
    OPENSEARCH_USER: Optional[str] = None
    OPENSEARCH_PASSWORD: Optional[str] = None
    OPENSEARCH_USE_SSL: bool = False
    OPENSEARCH_VERIFY_CERTS: bool = False

    OPENSEARCH_INDEX: str = "logs"
    OPENSEARCH_DEFAULT_TIME_RANGE_MINUTES: int = 15
    OPENSEARCH_MAX_LOG_LIMIT: int = 100

    # =========================
    # ✅ Vertex AI (Gemini)
    # =========================
    GOOGLE_CLOUD_PROJECT_ID: Optional[str] = None
    GOOGLE_CLOUD_LOCATION: str = "us-central1"
    GEMINI_MODEL_NAME: str = "gemini-1.5-pro"

    # =========================
    # ✅ OpenAI Settings
    # =========================
    OPENAI_API_KEY: Optional[str] = None
    OPENAI_MODEL: str = "gpt-4o-mini"

    # =========================
    # ✅ LLM Provider Control
    # =========================
    LLM_PROVIDER: str = "vertex"  # options: "vertex", "openai"

    # =========================
    # ✅ Agent Behavior Settings
    # =========================
    MAX_LOGS_FOR_ANALYSIS_LLM: int = 20
    LLM_TEMPERATURE: float = 0.2
    LLM_MAX_TOKENS: int = 1000

    # =========================
    # ✅ Future Scaling (optional)
    # =========================
    ENABLE_LLM_FALLBACK: bool = True
    # OpenAI (HCL AI Cafe)
    OPENAI_API_KEY: str
    OPENAI_BASE_URL: str
    OPENAI_MODEL: str = "gpt-4.1"

    # LLM control
    LLM_PROVIDER: str = "openai"

# Singleton instance
settings = Settings()