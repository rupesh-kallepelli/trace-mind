import os
import vertexai

from vertexai.generative_models import GenerativeModel

from app.core.config import settings


class VertexProvider:

    def __init__(self):

        os.environ[
            "GOOGLE_APPLICATION_CREDENTIALS"
        ] = settings.GOOGLE_APPLICATION_CREDENTIALS

        vertexai.init(
            project=settings.GOOGLE_CLOUD_PROJECT_ID,
            location=settings.GOOGLE_CLOUD_LOCATION
        )

        self.model = GenerativeModel(
            settings.VERTEX_MODEL
        )

    def chat(self, prompt: str):

        response = self.model.generate_content(prompt)

        return response.text