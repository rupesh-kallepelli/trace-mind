from kubernetes import client, config

config.load_kube_config()

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