from opensearchpy import OpenSearch
from opensearchpy.exceptions import NotFoundError

from app.core.config import settings


client = OpenSearch(
    hosts=[
        {
            "host": settings.OPENSEARCH_HOST,
            "port": settings.OPENSEARCH_PORT
        }
    ],
    use_ssl=False,
    verify_certs=False
)


class LogService:

    @staticmethod
    def fetch_logs(query: str):

        try:

            response = client.search(

                index="application-logs",

                body={
                    "size": 5,
                    "query": {
                        "match": {
                            "message": query
                        }
                    }
                }
            )

            return [
                hit["_source"]
                for hit in response["hits"]["hits"]
            ]

        ##################################################################
        # INDEX NOT FOUND
        ##################################################################

        except NotFoundError:

            print(
                "OpenSearch index "
                "'application-logs' does not exist yet"
            )

            return []

        ##################################################################
        # GENERIC FAILURE
        ##################################################################

        except Exception as ex:

            print(f"OpenSearch failure: {ex}")

            return []