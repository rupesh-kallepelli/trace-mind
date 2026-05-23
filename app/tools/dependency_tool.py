class DependencyTool:

    @staticmethod
    def blast_radius(graph, service):

        impacted = []

        if service in graph:
            impacted.extend(graph[service])

        return impacted