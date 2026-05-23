from langchain_google_vertexai import ChatVertexAI
from app.core.config import settings

llm = ChatVertexAI(
    model=settings.GEMINI_MODEL_NAME,
    project=settings.GOOGLE_CLOUD_PROJECT_ID,
    location=settings.GOOGLE_CLOUD_LOCATION,
    temperature=0
)

class RCAService:

    @staticmethod
    def generate(context):

        prompt = f'''

        You are an autonomous enterprise SRE.

        CONTEXT:
        {context}

        Generate:
        - root cause
        - blast radius
        - impacted services
        - confidence
        - remediation
        '''

        response = llm.invoke(prompt)

        return response.content