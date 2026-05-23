from sqlalchemy import create_engine, text
from app.core.config import settings

DATABASE_URL = (
    f"postgresql://{settings.POSTGRES_USER}:"
    f"{settings.POSTGRES_PASSWORD}@"
    f"{settings.POSTGRES_HOST}:"
    f"{settings.POSTGRES_PORT}/"
    f"{settings.POSTGRES_DB}"
)

engine = create_engine(DATABASE_URL)

SCHEMA = '''

CREATE EXTENSION IF NOT EXISTS vector;

CREATE TABLE IF NOT EXISTS incidents(
    id SERIAL PRIMARY KEY,
    issue TEXT,
    root_cause TEXT,
    confidence TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS incident_memory(
    id SERIAL PRIMARY KEY,
    issue TEXT,
    root_cause TEXT,
    fix TEXT,
    embedding vector(768)
);

CREATE TABLE IF NOT EXISTS source_memory(
    id SERIAL PRIMARY KEY,
    file_path TEXT,
    code_chunk TEXT,
    embedding vector(768)
);

'''

def initialize_database():

    with engine.begin() as conn:
        conn.execute(text(SCHEMA))