class KubernetesAnalysisTool:

    @staticmethod
    def detect_failures(pods):

        failures = []

        for pod in pods:

            status = pod.get("status")

            if status != "Running":
                failures.append(pod)

        return failures