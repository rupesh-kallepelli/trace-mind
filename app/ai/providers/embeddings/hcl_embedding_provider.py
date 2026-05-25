import requests

from app.core.config import settings


class HCLEmbeddingProvider:

    def __init__(self):

        self.url = (
            "https://aicafe.hcl.com/"
            "AICafeService/api/v1/subscription/openai/"
            f"deployments/{settings.HCL_EMBEDDING_DEPLOYMENT}"
            "/embeddings"
            f"?api-version={settings.HCL_EMBEDDING_API_VERSION}"
        )

    def embed(self, text: str):

        response = requests.post(

            self.url,

            headers={
                "api-key": settings.HCL_AI_CAFE_API_KEY,
                "Content-Type": "application/json"
            },

            json={
                "input": [
                    text
                ]
            },

            timeout=60
        )

        ##################################################################
        # FAILURE
        ##################################################################

        if response.status_code != 200:

            raise Exception(
                f"HCL Embedding API Failed: "
                f"{response.status_code} "
                f"{response.text}"
            )

        data = response.json()

        return data["data"][0]["embedding"]