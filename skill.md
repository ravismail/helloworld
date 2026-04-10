# Kubernetes AI-Enabled SRE Assistant

## Skill Name
k8s-ai-sre-observability

## Purpose
This skill enables an AI-powered Site Reliability Engineering (SRE) assistant to:

- Deploy as a DaemonSet inside a Kubernetes cluster (runs on every node)
- Authenticate via ServiceAccount with cluster-wide read-only RBAC
- Retrieve CPU and Memory metrics from Prometheus
- Fetch live logs for any namespace and pod
- Analyze pod manifests, related Kubernetes objects, logs, and metrics
- Provide AI-driven root cause analysis and recommendations via OpenAI (GPT-4o)
- Support interactive chat for dynamic, conversational SRE queries

## Architecture

### Tech Stack
| Layer | Technology |
|---|---|
| Backend | Python 3.12, FastAPI, Uvicorn |
| Frontend | React 18, Vite, Tailwind CSS, Recharts, Lucide Icons |
| AI | OpenAI GPT-4o (chat completions API) |
| K8s Client | `kubernetes` Python library (in-cluster config) |
| Metrics | Prometheus HTTP API via `httpx` |
| Deployment | DaemonSet (backend), Deployment (frontend), Kustomize |
| Containerization | Docker (multi-stage for frontend with Nginx) |

### Components

```
K8s-SRE/
├── backend/                        # Python FastAPI application
│   ├── app/
│   │   ├── main.py                 # FastAPI app, CORS, router registration
│   │   ├── config.py               # Pydantic settings (env-based config)
│   │   ├── models/schemas.py       # Request/response Pydantic models
│   │   ├── routers/
│   │   │   ├── kubernetes.py       # K8s resource endpoints + WebSocket log streaming
│   │   │   ├── metrics.py          # Prometheus CPU/memory query endpoints
│   │   │   └── analysis.py         # AI analysis + conversational chat endpoints
│   │   └── services/
│   │       ├── k8s_service.py      # Kubernetes client (lazy init, in-cluster first)
│   │       ├── prometheus_service.py  # Prometheus range/instant queries
│   │       └── ai_service.py       # OpenAI integration (analysis + chat)
│   ├── Dockerfile
│   └── requirements.txt
├── frontend/                       # React SPA
│   ├── src/
│   │   ├── App.jsx                 # Main layout (sidebar + content panels)
│   │   ├── components/
│   │   │   ├── Sidebar.jsx         # Namespace & pod selector
│   │   │   ├── PodHeader.jsx       # Pod status, node, containers, restarts
│   │   │   ├── MetricsPanel.jsx    # CPU/Memory time-series charts (Recharts)
│   │   │   ├── LogViewer.jsx       # Filterable log viewer with highlighting
│   │   │   ├── EventsPanel.jsx     # K8s events with warning indicators
│   │   │   ├── AiAnalysis.jsx      # One-click AI root cause analysis
│   │   │   └── ChatPanel.jsx       # Conversational AI chat interface
│   │   └── services/api.js         # API client (fetch wrapper)
│   ├── nginx.conf                  # Nginx reverse proxy to backend service
│   ├── Dockerfile
│   └── package.json
├── k8s/base/                       # Kubernetes manifests (Kustomize)
│   ├── namespace.yaml              # k8s-sre namespace
│   ├── serviceaccount.yaml         # ServiceAccount for backend pods
│   ├── clusterrole.yaml            # Cluster-wide read-only permissions
│   ├── clusterrolebinding.yaml     # Binds ClusterRole to ServiceAccount
│   ├── configmap.yaml              # Non-sensitive configuration
│   ├── secret.yaml                 # OpenAI API key
│   ├── backend-daemonset.yaml      # Backend DaemonSet (every node)
│   ├── backend-service.yaml        # ClusterIP service for backend
│   ├── frontend-deployment.yaml    # Frontend 2-replica Deployment
│   ├── frontend-service.yaml       # NodePort service (port 30080)
│   └── kustomization.yaml          # Kustomize orchestration
├── docker-compose.yml              # Local development with Docker Compose
├── deploy.sh                       # One-command cluster deployment script
└── skill.md                        # This file
```

## Capabilities

### 1. Kubernetes Resource Discovery
- List namespaces
- List pods within a namespace
- Retrieve:
  - Pod details (status, node, containers, restarts, age)
  - Pod manifest (full YAML)
  - Deployment / ReplicaSet owner chain
  - Services
  - ConfigMaps
  - Events (filtered by pod)

### 2. Metrics Collection (Prometheus Integration)
- Query Prometheus for CPU and memory usage at pod/container level
- Configurable time ranges: 5m, 15m, 30m, 1h, 3h, 6h, 24h
- Graceful degradation — returns empty data with error message if Prometheus is unreachable

Prometheus Queries Used:

```promql
# CPU usage per pod (rate over 5m window)
sum(rate(container_cpu_usage_seconds_total{namespace="$namespace", pod="$pod"}[5m])) by (pod)

# Memory usage per pod
sum(container_memory_usage_bytes{namespace="$namespace", pod="$pod"}) by (pod)
```

### 3. Live Logs
- Fetch logs by namespace, pod, and optional container
- Configurable tail lines (50, 100, 200, 500)
- Client-side filtering (search by keyword)
- Syntax highlighting: errors (red), warnings (yellow)
- Auto-scroll toggle
- WebSocket endpoint available for real-time streaming

### 4. AI-Powered SRE Analysis

#### One-Click Analysis
Gathers all pod data (logs, metrics, manifest, events, deployment) and sends it to OpenAI for structured root cause analysis.

Input sources:
- Pod logs (last 200 lines)
- CPU/Memory metrics from Prometheus
- Full pod manifest
- Deployment manifest (owner chain)
- Kubernetes events

Output format:
```json
{
  "summary": "Pod is crashing due to OOM",
  "root_cause": "Memory limit set to 512Mi but application consumes 600Mi+ under load",
  "confidence": "high",
  "metrics": {
    "cpu": "85m (within limits)",
    "memory": "512Mi / 512Mi (at limit)"
  },
  "recommendations": [
    "Increase memory limit to 768Mi",
    "Profile application for memory leaks",
    "Add memory-based HPA"
  ]
}
```

**Confidence Levels:**
| Level | Meaning |
|---|---|
| **High** | Strong corroborating evidence across logs, metrics, and events (e.g., OOMKilled + memory at limit) |
| **Medium** | Partial evidence — some signals correlate but data is incomplete |
| **Low** | Limited data available or multiple possible root causes |

#### Conversational Chat
Interactive chat panel for free-form SRE questions about the selected pod. Features:
- Full conversation history maintained per session
- Live pod context (logs, events, manifest) injected into every request
- Suggested starter questions (e.g., "Why is this pod crashing?")
- Chat resets automatically when switching pods
- Clear chat button

### 5. AI Query Examples

```
Why is my pod crashing in namespace prod-app?
Analyze high CPU usage for pod payment-service-abc123
Analyze recent logs and identify errors for pod user-service
Check if this deployment is configured correctly and suggest improvements
Is this pod resource-constrained?
Are the readiness/liveness probes configured correctly?
```

## AI Analysis Workflow

1. **User selects** a namespace and pod from the sidebar
2. **System gathers** (on "Run Analysis" click):
   - Pod logs (last 200 lines)
   - Prometheus metrics (CPU + memory for selected time range)
   - Full pod manifest
   - Deployment manifest (via owner reference chain)
   - Kubernetes events for the pod
3. **AI processes:**
   - Correlates logs with metrics
   - Detects patterns (OOMKilled, CrashLoopBackOff, ImagePullBackOff, throttling)
   - Validates manifest configuration
   - Identifies root cause
4. **AI outputs:**
   - Summary (one-line)
   - Root cause (detailed)
   - Confidence level (high / medium / low)
   - Metrics summary
   - Actionable recommendations

## API Endpoints

### Kubernetes
| Method | Path | Description |
|---|---|---|
| GET | `/api/k8s/namespaces` | List all namespaces |
| GET | `/api/k8s/namespaces/{ns}/pods` | List pods in namespace |
| GET | `/api/k8s/namespaces/{ns}/pods/{pod}` | Pod details |
| GET | `/api/k8s/namespaces/{ns}/pods/{pod}/manifest` | Full pod manifest |
| GET | `/api/k8s/namespaces/{ns}/pods/{pod}/logs` | Pod logs (query: container, tail_lines) |
| GET | `/api/k8s/namespaces/{ns}/pods/{pod}/events` | Pod events |
| GET | `/api/k8s/namespaces/{ns}/pods/{pod}/deployment` | Owner deployment |
| GET | `/api/k8s/namespaces/{ns}/services` | List services |
| GET | `/api/k8s/namespaces/{ns}/configmaps` | List configmaps |
| WS | `/api/k8s/namespaces/{ns}/pods/{pod}/logs/stream` | WebSocket log stream |

### Metrics
| Method | Path | Description |
|---|---|---|
| GET | `/api/metrics/cpu/{ns}/{pod}` | CPU usage (query: time_range) |
| GET | `/api/metrics/memory/{ns}/{pod}` | Memory usage (query: time_range) |
| GET | `/api/metrics/query` | Custom PromQL query |

### Analysis
| Method | Path | Description |
|---|---|---|
| POST | `/api/analysis/analyze` | Full AI root cause analysis |
| POST | `/api/analysis/chat` | Conversational AI chat |
| GET | `/api/health` | Health check |

### Request/Response Schemas

**Analysis Request:**
```json
{
  "namespace": "string",
  "pod": "string",
  "time_range": "last_5m | last_15m | last_1h | last_3h",
  "include_logs": true,
  "include_metrics": true
}
```

**Chat Request:**
```json
{
  "namespace": "string",
  "pod": "string",
  "message": "Why is this pod crashing?",
  "history": [
    {"role": "user", "content": "previous question"},
    {"role": "assistant", "content": "previous answer"}
  ]
}
```

**Chat Response:**
```json
{
  "reply": "Based on the logs, your pod is crash-looping because..."
}
```

## Kubernetes Deployment

### RBAC Permissions (ClusterRole: k8s-sre-reader)
Read-only access across all namespaces:

| API Group | Resources | Verbs |
|---|---|---|
| `""` (core) | namespaces, pods, pods/log, services, configmaps, secrets, events, endpoints, nodes, PVCs, PVs, resourcequotas, limitranges, replicationcontrollers | get, list, watch |
| `apps` | deployments, replicasets, statefulsets, daemonsets | get, list, watch |
| `batch` | jobs, cronjobs | get, list, watch |
| `autoscaling` | horizontalpodautoscalers | get, list, watch |
| `networking.k8s.io` | ingresses, networkpolicies | get, list, watch |
| `metrics.k8s.io` | nodes, pods | get, list |

### Deployment Topology
- **Backend**: DaemonSet — one pod per node (including control-plane via tolerations)
  - ServiceAccount: `k8s-sre-sa` with ClusterRoleBinding
  - In-cluster config (no kubeconfig needed)
  - Resource limits: 100m-500m CPU, 128Mi-512Mi memory
  - Health probes on `/api/health`
- **Frontend**: Deployment (2 replicas)
  - Nginx serves static React build
  - Reverse proxy to backend via K8s service DNS
  - Exposed via NodePort 30080

### Deployment Commands
```bash
# One-command deploy
export OPENAI_API_KEY=sk-...
./deploy.sh

# Or manual
docker build -t k8s-sre-backend ./backend
docker build -t k8s-sre-frontend ./frontend
kubectl apply -k k8s/base

# Set the API key secret
kubectl -n k8s-sre create secret generic k8s-sre-secret \
  --from-literal=OPENAI_API_KEY="$OPENAI_API_KEY" \
  --dry-run=client -o yaml | kubectl apply -f -

# Access
kubectl -n k8s-sre port-forward svc/k8s-sre-frontend 3000:80
# Or via NodePort: http://<node-ip>:30080
```

### Local Development (Docker Compose)
```bash
cd backend && cp .env.example .env  # Set OPENAI_API_KEY
docker compose up --build
# Frontend: http://localhost:3000
# Backend:  http://localhost:8001
```

## Configuration

### Environment Variables
| Variable | Default | Description |
|---|---|---|
| `PROMETHEUS_URL` | `http://prometheus.default.svc.cluster.local:9090` | Prometheus server URL |
| `OPENAI_API_KEY` | (required) | OpenAI API key |
| `OPENAI_MODEL` | `gpt-4o` | OpenAI model to use |
| `KUBECONFIG_PATH` | (auto-detect) | Path to kubeconfig (not needed in-cluster) |
| `LOG_TAIL_LINES` | `200` | Default number of log lines to fetch |
| `CORS_ORIGINS` | `["http://localhost:5173"]` | Allowed CORS origins |

### Kubernetes Config Priority
1. In-cluster config (ServiceAccount token) — used when deployed as DaemonSet
2. Explicit `KUBECONFIG_PATH` — for external/local development
3. Default `~/.kube/config` — fallback for local development

## Security Considerations
- RBAC enforces **read-only** access — no write/delete/exec permissions
- ServiceAccount scoped to `k8s-sre` namespace, ClusterRole for cross-namespace reads
- OpenAI API key stored in Kubernetes Secret (not ConfigMap)
- Pod manifests are trimmed before sending to AI (spec + status only in chat)
- No secrets values are sent to AI — only secret names from configmap listings
- Prometheus endpoint accessed internally within cluster network
- Frontend proxies all API calls through Nginx (no direct backend exposure)

## Future Enhancements
- Auto-remediation (restart pod, scale deployment) with write RBAC opt-in
- Anomaly detection using ML on historical metrics
- Slack / Teams integration for alerts and chat
- Incident timeline generation from correlated events
- Cost optimization insights (resource right-sizing)
- Loki integration for centralized log aggregation
- Multi-cluster support
- Persistent chat history with conversation export
- Streaming AI responses (SSE/WebSocket)
