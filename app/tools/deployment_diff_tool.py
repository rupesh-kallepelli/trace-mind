class DeploymentDiffTool:

    @staticmethod
    def analyze(before, after):

        return {
            "changed_services": [
                "payment-service"
            ],
            "risk": "MEDIUM"
        }