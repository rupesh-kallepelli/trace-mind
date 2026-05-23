class DependencyService:

    @staticmethod
    def build_graph():

        return {
            "payment-service": [
                "inventory-service",
                "postgres",
                "redis"
            ]
        }