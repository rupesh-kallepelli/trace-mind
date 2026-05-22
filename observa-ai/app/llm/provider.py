import logging
from ..config.settings import settings

logger = logging.getLogger(__name__)

# Lazy initialization
_openai_client = None
_vertex_client = None


def get_client():
    global _openai_client, _vertex_client

    if settings.LLM_PROVIDER == "openai":
        if _openai_client is None:
            from app.llm.openai_client import OpenAIClient
            _openai_client = OpenAIClient()
        return _openai_client

    elif settings.LLM_PROVIDER == "vertex":
        if _vertex_client is None:
            from app.llm.vertex_client import VertexAIClient
            _vertex_client = VertexAIClient()
        return _vertex_client

    else:
        raise ValueError("Invalid LLM_PROVIDER")


async def call_llm(prompt: str) -> str:
    client = get_client()

    if settings.LLM_PROVIDER == "openai":
        return await client.generate_content(prompt)

    else:
        return await client.generate_content_with_retry(prompt)


async def call_llm_json(prompt: str) -> str:
    client = get_client()

    if settings.LLM_PROVIDER == "openai":
        return await client.generate_json(prompt)

    else:
        return await client.generate_content_with_retry(prompt)