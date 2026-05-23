from langchain_google_vertexai import VertexAIEmbeddings
from app.core.config import settings

embedding_model = VertexAIEmbeddings(
    model_name="textembedding-gecko@003",
    project=settings.GOOGLE_CLOUD_PROJECT_ID,
    location=settings.GOOGLE_CLOUD_LOCATION
)