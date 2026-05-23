from pydantic_settings import BaseSettings

class Settings(BaseSettings):

    GOOGLE_APPLICATION_CREDENTIALS: str
    GOOGLE_CLOUD_PROJECT_ID: str
    GOOGLE_CLOUD_LOCATION: str
    GEMINI_MODEL_NAME: str

    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str

    OPENSEARCH_HOST: str
    OPENSEARCH_PORT: int

    GITHUB_TOKEN: str
    GITHUB_REPO: str

    JIRA_URL: str
    JIRA_USERNAME: str
    JIRA_API_TOKEN: str

    class Config:
        env_file = ".env"

settings = Settings()