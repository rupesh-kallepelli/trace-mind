# ObservaAI Infrastructure

This infrastructure is optimized for:
- OpenShift Free Trial
- Low memory footprint
- Single-node OpenSearch
- Lightweight PGVector deployment

## Components
- PostgreSQL + PGVector
- OpenSearch
- Backend
- Frontend
- RBAC
- Routes
- Services
- PVCs
- Secrets

## Deploy

```bash
helm upgrade --install observaai-platform infra/helm/observaai-platform
```

## GitHub Secrets Required

- OPENSHIFT_API
- OPENSHIFT_TOKEN
- OPENSHIFT_NAMESPACE