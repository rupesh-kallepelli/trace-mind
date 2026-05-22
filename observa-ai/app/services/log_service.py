from opensearchpy import OpenSearch
from typing import List, Dict

client = OpenSearch(
    hosts=[{"host": "localhost", "port": 9200}],
    http_compress=True,
    use_ssl=False,
    verify_certs=False
)


def get_logs(keyword: str) -> List[Dict]:

    query = {
        "query": {
            "match": {
                "message": keyword
            }
        },
        "size": 20
    }

    response = client.search(index="logs", body=query)

    return [hit["_source"] for hit in response["hits"]["hits"]]