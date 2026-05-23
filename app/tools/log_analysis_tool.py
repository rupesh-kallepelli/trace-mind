class LogAnalysisTool:

    @staticmethod
    def cluster_errors(logs):

        grouped = {}

        for log in logs:
            grouped[log] = grouped.get(log, 0) + 1

        return grouped