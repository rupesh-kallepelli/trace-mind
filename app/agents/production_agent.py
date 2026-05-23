from app.graph.workflow import graph

class ProductionSupportAgent:

    @staticmethod
    def analyze(issue):

        result = graph.invoke({
            "issue": issue
        })

        return result