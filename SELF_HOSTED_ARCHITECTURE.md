# Self Hosted Platform Components

## Fully Self Hosted

- PostgreSQL
- PGVector
- OpenSearch
- JIRA Software
- Redis
- MinIO
- Backend
- Frontend

## External

- Vertex AI Gemini
- GitHub Repository

## Integration Flow

Frontend
  ↓
Backend API
  ↓
LangGraph AI Engine
  ↓
OpenSearch + PGVector + JIRA + Kubernetes + GitHub

## OpenShift Optimizations

- low memory limits
- single-node deployments
- lightweight PVC sizing
- OpenSearch heap tuning
- non-root compatible containers

## Important

JIRA is memory intensive.
Recommended:
- minimum 1Gi memory
- preferably deploy after core platform stabilizes