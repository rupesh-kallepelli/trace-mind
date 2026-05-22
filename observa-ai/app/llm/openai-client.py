import logging
from typing import Any, Dict
import httpx
from ..config.settings import settings

logger = logging.getLogger(__name__)


class OpenAIClient:
    """
    Custom OpenAI client for HCL AI Cafe endpoint
    """

    def __init__(self):
        if not settings.OPENAI_API_KEY:
            raise RuntimeError("OPENAI_API_KEY not set")

        self.base_url = settings.OPENAI_BASE_URL  # ✅ IMPORTANT
        self.api_key = settings.OPENAI_API_KEY

        self.client = httpx.AsyncClient(
            base_url=self.base_url,
            timeout=30.0,
            headers={
                "api-key": self.api_key,   # ✅ Azure-style header
                "Content-Type": "application/json"
            }
        )

        logger.info("HCL OpenAI client initialized")

    async def generate_content(self, prompt: str) -> str:
        try:
            payload = {
                "messages": [
                    {
                        "role": "system",
                        "content": "You are an expert AI for observability and debugging."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                "temperature": 0.2,
                "max_tokens": 1000
            }

            response = await self.client.post("", json=payload)

            response.raise_for_status()

            data = response.json()

            return data["choices"][0]["message"]["content"].strip()

        except Exception as e:
            logger.error(f"HCL OpenAI API error: {e}", exc_info=True)
            raise RuntimeError(f"OpenAI request failed: {e}")
