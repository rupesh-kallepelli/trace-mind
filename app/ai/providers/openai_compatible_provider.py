from openai import OpenAI


class OpenAICompatibleProvider:

    def __init__(
        self,
        api_key: str,
        base_url: str,
        model: str
    ):

        self.model = model

        self.client = OpenAI(
            api_key=api_key,
            base_url=base_url
        )

    def chat(self, prompt: str):

        response = self.client.chat.completions.create(

            model=self.model,

            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],

            temperature=0.3,
            max_tokens=1500
        )

        return response.choices[0].message.content