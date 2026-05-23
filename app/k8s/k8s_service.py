from kubernetes import client, config
from kubernetes.config.config_exception import ConfigException


class KubernetesService:

    def __init__(self):

        try:

            config.load_incluster_config()

            print("Using in-cluster config")

        except ConfigException:

            config.load_kube_config()

            print("Using local kubeconfig")

        self.v1 = client.CoreV1Api()

    def cluster_analysis(self):

        pods = self.v1.list_pod_for_all_namespaces()

        results = []

        for pod in pods.items:

            if pod.status.phase != "Running":

                results.append({
                    "pod": pod.metadata.name,
                    "status": pod.status.phase
                })

        return results