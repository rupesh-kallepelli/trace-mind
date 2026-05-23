K8S_ANALYSIS_PROMPT = '''
Analyze Kubernetes/OpenShift failures.

Focus on:
- CrashLoopBackOff
- OOMKilled
- deployment rollout failures
- pod restarts
- replica mismatch
- unhealthy nodes
- configuration drift
'''