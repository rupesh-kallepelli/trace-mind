import os

from kubernetes import client, config
from kubernetes.config.config_exception import ConfigException


##################################################################
# LOCAL / CLUSTER CONFIG
##################################################################

if os.getenv("ENVIRONMENT", "local") == "local":

    config.load_kube_config()

    print("Using local kubeconfig")

else:

    configuration = client.Configuration()

    configuration.host = os.getenv(
        "K8S_HOST",
        "https://kubernetes.default.svc"
    )

    with open(
        os.getenv(
            "K8S_TOKEN_PATH",
            "/app/k8s-auth/token"
        )
    ) as f:

        token = f.read()

    configuration.api_key = {
        "authorization": token
    }

    configuration.api_key_prefix = {
        "authorization": "Bearer"
    }

    configuration.ssl_ca_cert = os.getenv(
        "K8S_CA_CERT",
        "/app/k8s-auth/ca.crt"
    )

    client.Configuration.set_default(configuration)

    print("Using in-cluster auth")

##################################################################
# CLIENT
##################################################################

v1 = client.CoreV1Api()


class KubernetesService:

    @staticmethod
    def cluster_analysis():

        namespace = os.getenv(
            "K8S_NAMESPACE",
            "kallepelli-rupesh-dev"
        )

        ##################################################################
        # ONLY CURRENT NAMESPACE
        ##################################################################

        pods = v1.list_namespaced_pod(
            namespace=namespace
        )

        results = []

        for pod in pods.items:

            if pod.status.phase != "Running":

                results.append({
                    "pod": pod.metadata.name,
                    "status": pod.status.phase
                })

        return results