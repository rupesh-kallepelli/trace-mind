import google.generativeai as genai
import logging
from google.api_core.exceptions import GoogleAPIError
from ..config.settings import settings

logger = logging.getLogger(__name__)

class VertexAIClient:
    """
    Client for interacting with Google's Vertex AI Gemini model.
    Assumes GOOGLE_APPLICATION_CREDENTIALS environment variable is set for authentication.
    """

    def __init__(self):
        if not settings.GOOGLE_CLOUD_PROJECT_ID:
            logger.warning("GOOGLE_CLOUD_PROJECT_ID not set. Vertex AI client might fail.")
        try:
            genai.configure(
                project=settings.GOOGLE_CLOUD_PROJECT_ID,
                location=settings.GOOGLE_CLOUD_LOCATION
            )
            self.model = genai.GenerativeModel(settings.GEMINI_MODEL_NAME)
            logger.info(f"Vertex AI Gemini client initialized with model: {settings.GEMINI_MODEL_NAME}")
        except Exception as e:
            logger.error(f"Failed to configure Vertex AI: {e}", exc_info=True)
            raise RuntimeError(f"Failed to initialize Vertex AI client: {e}")

    def get_model(self) -> genai.GenerativeModel:
        """Returns the configured Gemini GenerativeModel instance."""
        return self.model

    async def generate_content_with_retry(self, prompt: str, **kwargs) -> str:
        """
        Sends a prompt to the Gemini model and handles retries.
        For a real production system, consider implementing robust retry logic
        using a library like 'tenacity' or 'google-api-core.retry'.
        """
        try:
            response = await self.model.generate_content_async(prompt, **kwargs)
            return response.text
        except GoogleAPIError as e:
            logger.error(f"Vertex AI API error: {e}", exc_info=True)
            raise RuntimeError(f"Vertex AI API call failed: {e}")
        except Exception as e:
            logger.error(f"An unexpected error occurred during LLM call: {e}", exc_info=True)
            raise RuntimeError(f"LLM content generation failed: {e}")
