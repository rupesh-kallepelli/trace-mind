from opensearchpy import OpenSearch
from app.core.config import settings

client = OpenSearch(
    hosts=[{
        "host": settings.OPENSEARCH_HOST,
        "port": settings.OPENSEARCH_PORT
    }]
)

class LogService:

    @staticmethod
    def fetch_logs(issue):

        query = {
            "query": {
                "match": {
                    "message": issue
                }
            },
            "size": 20
        }

        response = client.search(
            index="application-logs",
            body=query
        )

        return [
            hit["_source"]["message"]
            for hit in response["hits"]["hits"]
        ]