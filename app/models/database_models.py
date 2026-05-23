from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, Text

Base = declarative_base()


class IncidentMemory(Base):

    __tablename__ = "incident_memory"

    id = Column(Integer, primary_key=True)
    issue = Column(Text)
    root_cause = Column(Text)
    remediation = Column(Text)


class SourceMemory(Base):

    __tablename__ = "source_memory"

    id = Column(Integer, primary_key=True)
    file_path = Column(Text)
    chunk = Column(Text)