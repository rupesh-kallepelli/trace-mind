from app.core.config import settings

from app.ai.providers.embeddings.hcl_embedding_provider import (
    HCLEmbeddingProvider
)

from app.ai.providers.embeddings.vertex_embedding_provider import (
    VertexEmbeddingProvider
)


class EmbeddingFactory:

    @staticmethod
    def get_provider():

        provider = settings.LLM_PROVIDER.lower()

        ##################################################################
        # HCL
        ##################################################################

        if provider == "hcl":
            return HCLEmbeddingProvider()

        ##################################################################
        # VERTEX
        ##################################################################

        elif provider == "vertex":
            return VertexEmbeddingProvider()

        raise Exception(
            f"Unsupported embedding provider: {provider}"
        )