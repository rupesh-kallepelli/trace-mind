from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    ##################################################################
    # ACTIVE PROVIDER
    ##################################################################

    LLM_PROVIDER: str = "hcl"

    ##################################################################
    # HCL AI CAFE
    ##################################################################

    HCL_AI_CAFE_API_KEY: str = ""
    HCL_AI_CAFE_MODEL: str = "gpt-4.1"

    ##################################################################
    # OPENROUTER
    ##################################################################

    OPENROUTER_API_KEY: str = ""
    OPENROUTER_BASE_URL: str = "https://openrouter.ai/api/v1"
    OPENROUTER_MODEL: str = "openai/gpt-4o-mini"

    ##################################################################
    # VERTEX AI
    ##################################################################

    GOOGLE_APPLICATION_CREDENTIALS: str = ""
    GOOGLE_CLOUD_PROJECT_ID: str = ""
    GOOGLE_CLOUD_LOCATION: str = "us-central1"
    VERTEX_MODEL: str = "gemini-1.5-pro"

    ##################################################################
    # POSTGRES
    ##################################################################

    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str

    ##################################################################
    # OPENSEARCH
    ##################################################################

    OPENSEARCH_HOST: str
    OPENSEARCH_PORT: int

    ##################################################################
    # GITHUB
    ##################################################################

    GITHUB_TOKEN: str
    GITHUB_REPO: str

    ##################################################################
    # JIRA
    ##################################################################

    JIRA_URL: str = ""
    JIRA_USERNAME: str = ""
    JIRA_API_TOKEN: str = ""
    JIRA_ENABLED: bool = False
    ENABLE_EMBEDDINGS: bool = False

    class Config:
        env_file = ".env"
        extra = "ignore"

settings = Settings()