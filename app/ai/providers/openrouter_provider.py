from app.core.config import settings

from app.ai.providers.openai_compatible_provider import (
    OpenAICompatibleProvider
)


class OpenRouterProvider(OpenAICompatibleProvider):

    def __init__(self):

        super().__init__(
            api_key=settings.OPENROUTER_API_KEY,
            base_url=settings.OPENROUTER_BASE_URL,
            model=settings.OPENROUTER_MODEL
        )