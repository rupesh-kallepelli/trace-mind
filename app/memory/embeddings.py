from app.ai.providers.embeddings.embedding_factory import (
    EmbeddingFactory
)

embedding_model = (
    EmbeddingFactory.get_provider()
)