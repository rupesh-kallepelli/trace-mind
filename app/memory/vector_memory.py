from sqlalchemy import text
from app.db.database import engine
from app.memory.embeddings import embedding_model

class VectorMemory:

    @staticmethod
    def store_incident(issue, root_cause, fix):

        embedding = embedding_model.embed_query(issue)

        query = text(
            '''
            INSERT INTO incident_memory
            (issue, root_cause, fix, embedding)
            VALUES
            (:issue, :root_cause, :fix, :embedding)
            '''
        )

        with engine.begin() as conn:
            conn.execute(query, {
                "issue": issue,
                "root_cause": root_cause,
                "fix": fix,
                "embedding": embedding
            })

    @staticmethod
    def search_similar(issue):

        embedding = embedding_model.embed_query(issue)

        query = text(
            '''
            SELECT issue, root_cause, fix
            FROM incident_memory
            ORDER BY embedding <-> :embedding
            LIMIT 5
            '''
        )

        with engine.begin() as conn:
            rows = conn.execute(query, {
                "embedding": embedding
            }).fetchall()

        return [dict(row._mapping) for row in rows]