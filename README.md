# ObservaAI Enterprise

Autonomous Enterprise Production Support Engineer.

## Enterprise Capabilities

- LangGraph deterministic orchestration
- Multi-agent AI system
- Historical incident memory
- Semantic vector retrieval
- JIRA intelligence learning
- GitHub semantic code ingestion
- Kubernetes/OpenShift analysis
- Blast radius analysis
- Deployment risk analysis
- Timeline reconstruction
- OpenSearch observability
- PGVector semantic memory
- OpenShift-native deployment

## Architecture

FastAPI
 ↓
LangGraph Workflow Engine
 ↓
Agents
 ├── Log Agent
 ├── JIRA Agent
 ├── Code Agent
 ├── Kubernetes Agent
 ├── Memory Agent
 └── RCA Agent
 ↓
PGVector + OpenSearch + PostgreSQL

## Run Locally

```bash
cp .env.example .env
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## OpenShift Deployment

```bash
oc new-project observaai

oc apply -f openshift/

helm install observaai helm/observaai
```

## Frontend UI

### Features
- Live dashboard
- Incident table
- Dependency visualization APIs
- Cluster health monitoring

### Run Frontend

```bash
cd frontend
npm install
npm run dev
```

Frontend URL:
http://localhost:3000


# Real System Integrations

## Supported Integrations

### Kubernetes/OpenShift
- Namespace-aware analysis
- Pod health analysis
- CrashLoopBackOff detection
- Deployment analysis

### GitHub
- Semantic repository ingestion
- Source-code embeddings
- Deployment diff preparation

### JIRA
- Historical incident retrieval
- RCA learning
- Operational intelligence

### OpenSearch
- Real-time log analysis
- Incident correlation
- Error clustering

### PostgreSQL + PGVector
- Semantic memory
- Historical incident retrieval
- Source-code vector search

# OpenShift Deployment

```bash
oc apply -f openshift/
```

# Frontend

```bash
cd frontend
npm install
npm run dev
```

Frontend:
http://localhost:3000


# Backend Connectivity Fix

Added:
- backend deployment
- backend service
- backend route
- frontend environment configuration
- centralized API configuration

Frontend now connects using:

```txt
VITE_API_BASE_URL
```

OpenShift backend service:

```txt
observaai-backend:8000
```


# AI Prompt Layer

Added dedicated prompts for:
- RCA generation
- Kubernetes analysis
- Deployment risk analysis
- JIRA intelligence
- Memory retrieval

# Tooling Layer

Added backend tools for:
- log clustering
- dependency blast radius
- deployment diff analysis
- incident correlation
- Kubernetes failure analysis

This improves:
- modularity
- prompt engineering
- AI reasoning consistency
- enterprise maintainability


# Model Layer

Added enterprise-grade model structure:

## Request Models
- AnalyzeRequest

## Response Models
- RCAResponse
- DashboardSummary
- IncidentModel
- TimelineEvent

## Entity Models
- IncidentEntity
- SourceCodeEntity
- KubernetesPodEntity
- JiraIncidentEntity
- DependencyEntity

## AI Models
- AgentStateModel
- EmbeddingDocument

## Database Models
- IncidentMemory
- SourceMemory

Benefits:
- strong typing
- enterprise maintainability
- API contract consistency
- scalable architecture
- easier frontend/backend integration


# GitHub Actions CI/CD

## Backend Workflow
.github/workflows/backend-ci-cd.yaml

## Frontend Workflow
.github/workflows/frontend-ci-cd.yaml

Required GitHub Secrets:
- OPENSHIFT_API
- OPENSHIFT_TOKEN

# Frontend OpenShift Resources
- frontend deployment
- frontend service
- frontend route
- frontend imagestream
- frontend buildconfig

# Final Recommendations
Refer:
ARCHITECTURE_REVIEW.md
