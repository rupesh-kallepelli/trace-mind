from github import Github
from app.core.config import settings
from app.memory.embeddings import embedding_model
from app.db.database import engine
from sqlalchemy import text

github_client = Github(settings.GITHUB_TOKEN)

class GitHubIngestionService:

    @staticmethod
    def ingest_repository():

        repo = github_client.get_repo(
            settings.GITHUB_REPO
        )

        contents = repo.get_contents("")

        while contents:

            item = contents.pop(0)

            if item.type == "dir":
                contents.extend(
                    repo.get_contents(item.path)
                )
                continue

            try:

                code = item.decoded_content.decode("utf-8")

                chunks = [
                    code[i:i+1000]
                    for i in range(0, len(code), 1000)
                ]

                for chunk in chunks:

                    embedding = embedding_model.embed(chunk)

                    query = text(
                        '''
                        INSERT INTO source_memory
                        (file_path, code_chunk, embedding)
                        VALUES
                        (:file_path, :code_chunk, :embedding)
                        '''
                    )

                    with engine.begin() as conn:
                        conn.execute(query, {
                            "file_path": item.path,
                            "code_chunk": chunk,
                            "embedding": embedding
                        })

            except Exception:
                continue