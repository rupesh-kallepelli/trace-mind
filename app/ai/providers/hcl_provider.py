import requests

from app.core.config import settings


class HCLAICafeProvider:

    def __init__(self):

        self.url = (
            "https://aicafe.hcl.com/"
            "AICafeService/api/v1/subscription/openai/"
            "deployments/gpt-4.1/chat/completions"
            "?api-version=2024-12-01-preview"
        )

    def chat(self, prompt: str):

        response = requests.post(

            self.url,

            headers={
                "api-key": settings.HCL_AI_CAFE_API_KEY,
                "Content-Type": "application/json"
            },

            json={
                "model": "gpt-4.1",

                "messages": [
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],

                "maxTokens": 1000,
                "temperature": 0.3
            },

            timeout=120
        )

        ##################################################################
        # FAILURE
        ##################################################################

        if response.status_code != 200:

            raise Exception(
                f"HCL AI Cafe failed: "
                f"{response.status_code} "
                f"{response.text}"
            )

        data = response.json()

        return (
            data["choices"][0]
            ["message"]
            ["content"]
        )