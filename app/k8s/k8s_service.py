from kubernetes import client

configuration = client.Configuration()

configuration.host = "https://kubernetes.default.svc"

with open("/app/k8s-auth/token") as f:
    token = f.read()

configuration.api_key = {
    "authorization": token
}

configuration.api_key_prefix = {
    "authorization": "Bearer"
}

configuration.ssl_ca_cert = "/app/k8s-auth/ca.crt"

client.Configuration.set_default(configuration)

v1 = client.CoreV1Api()


class KubernetesService:

    @staticmethod
    def cluster_analysis():

        pods = v1.list_pod_for_all_namespaces()

        results = []

        for pod in pods.items:

            if pod.status.phase != "Running":

                results.append({
                    "pod": pod.metadata.name,
                    "status": pod.status.phase
                })

        return results