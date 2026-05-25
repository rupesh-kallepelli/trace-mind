from app.core.config import settings

from app.ai.providers.hcl_provider import (
    HCLAICafeProvider
)

from app.ai.providers.openrouter_provider import (
    OpenRouterProvider
)

from app.ai.providers.vertex_provider import (
    VertexProvider
)


class ProviderFactory:

    @staticmethod
    def get_provider():

        provider = settings.LLM_PROVIDER.lower()

        ##################################################################
        # HCL AI CAFE
        ##################################################################

        if provider == "hcl":
            return HCLAICafeProvider()

        ##################################################################
        # OPENROUTER
        ##################################################################

        elif provider == "openrouter":
            return OpenRouterProvider()

        ##################################################################
        # VERTEX AI
        ##################################################################

        elif provider == "vertex":
            return VertexProvider()

        raise Exception(f"Unsupported provider: {provider}")