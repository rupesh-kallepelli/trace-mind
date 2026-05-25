from app.graph.workflow import graph

from app.ai.providers.provider_factory import (
    ProviderFactory
)


class ProductionSupportAgent:

    @staticmethod
    def analyze(issue):

        provider = ProviderFactory.get_provider()

        result = graph.invoke({
            "issue": issue,
            "provider": provider
        })

        return result