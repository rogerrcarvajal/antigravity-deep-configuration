# Multi-Archetype Tech Stack & Cloud-Native Architectural Guidelines

Esta especificación técnica rige los estándares de arquitectura, lenguajes, frameworks, seguridad y despliegue en la nube para los proyectos desarrollados en el ecosistema de Google Antigravity.

Opera bajo un modelo **Multi-Arquetipo Adaptativo**, permitiendo que proyectos empresariales transaccionales tradicionales (ej. CEIA_SWGA) y soluciones modernas nativas de nube con agentes inteligentes (ej. Wellness Platform 2.0 / Nutrition Agent) coexistan con excelencia de ingeniería sin fricción.

---

## 🧭 Matriz de Detección y Selección de Arquetipo

Antigravity y sus agentes identifican automáticamente el arquetipo aplicable al iniciar o intervenir un proyecto:

| Arquetipo | Indicadores de Detección | Stack Principal | Paradigma |
|---|---|---|---|
| **Arquetipo A: Core Web & Enterprise Transaccional**<br>*(Línea Base CEIA / SWGA)* | Archivos `*.php`, `composer.json`, Apache/XAMPP, esquemas SQL tradicionales. | PHP 8.2+ POO/MVC, PostgreSQL 14+, HTML5, CSS3, JS Vanilla. | MVC desacoplado, PDO Prepared Statements, PSR-4/7/12/15, monolithic/modular. |
| **Arquetipo B: Cloud-Native & Intelligent Agent Ecosystem**<br>*(Línea Base Wellness 2.0 / Proyectos de Vanguardia)* | Archivos `*.py`, `pyproject.toml`, `requirements.txt`, FastAPI, Dockerfile, RAG/LLM. | Python 3.11+, FastAPI asíncrono, Pydantic v2, PostgreSQL + pgvector, Redis, HTML5/CSS3 Glassmorphic. | Cloud-Native, Agent-First, Event-Driven, Microservicios asíncronos, despliegue Multi-Cloud (GCP/AWS). |

---

## 🏛️ Arquetipo A: Core Web & Enterprise Transaccional (CEIA / SWGA)

> [!NOTE]
> Este arquetipo representa la línea base institucional y académica probada para proyectos transaccionales, garantizando estabilidad y cero regresiones en sistemas existentes.

### 1. Stack Técnico Detallado

| Capa | Tecnología | Directrices Obligatorias |
|---|---|---|
| **Backend** | PHP 8.2+ | Programación Orientada a Objetos (POO), `declare(strict_types=1);`, patrón MVC. |
| **Web Server** | Apache / Nginx (XAMPP local) | Mod_rewrite activo, `DocumentRoot` configurado hacia `public/` o raíz controlada. |
| **Database** | PostgreSQL 14+ / MariaDB | Integridad referencial estricta, claves foráneas, índices explícitos, transacciones ACID. |
| **Frontend** | HTML5 semántico & CSS3 | JavaScript Vanilla moderno, diseño responsivo, sin frameworks pesados innecesarios. |
| **Tooling** | Antigravity / Composer | PSR-4 (autoload), PSR-12 (formato), PHP Intelephense, PHPUnit. |

### 2. Estándar de Controlador (PHP 8.2+ POO & MVC)

```php
<?php
declare(strict_types=1);

namespace App\Controllers;

use App\Models\EstudianteModel;
use App\Services\ResponseService;

class EstudianteController
{
    private EstudianteModel $estudianteModel;

    public function __construct(EstudianteModel $estudianteModel)
    {
        $this->estudianteModel = $estudianteModel;
    }

    public function index(): void
    {
        $estudiantes = $this->estudianteModel->getAllActive();
        ResponseService::json([
            'success' => true,
            'data' => $estudiantes,
            'message' => 'Lista de estudiantes activos recuperada exitosamente'
        ]);
    }
}
```

### 3. Capa de Datos Segura (PostgreSQL & PDO)

```php
<?php
declare(strict_types=1);

namespace App\Models;

use PDO;

class EstudianteModel
{
    private PDO $db;

    public function __construct(PDO $db)
    {
        $this->db = $db;
    }

    public function findById(int $id): ?array
    {
        $stmt = $this->db->prepare("
            SELECT id, cedula, nombres, apellidos, email, fecha_registro
            FROM estudiantes
            WHERE id = :id AND activo = true
            LIMIT 1
        ");
        $stmt->execute(['id' => $id]);
        $result = $stmt->fetch(PDO::FETCH_ASSOC);

        return $result ?: null;
    }
}
```

```sql
-- Índices obligatorios en claves foráneas y columnas de filtrado frecuente
CREATE INDEX IF NOT EXISTS idx_estudiantes_cedula ON estudiantes(cedula);
CREATE INDEX IF NOT EXISTS idx_estudiantes_activo ON estudiantes(activo);
```

---

## ⚡ Arquetipo B: Cloud-Native, AI-First & Intelligent Agent Ecosystem (Vanguardia)

> [!IMPORTANT]
> Este arquetipo rige los nuevos desarrollos de software basados en agentes autónomos, inferencia de modelos de IA, contenedorización y despliegue automatizado a nubes públicas (Google Cloud Platform, AWS, Azure, etc.).

### 1. Stack Técnico Cloud-Native de Vanguardia

| Capa | Tecnología | Directrices de Ingeniería |
|---|---|---|
| **Núcleo de IA & Agentes** | Python 3.11+ / 3.12+ | Asincronía nativa (`async def`), Pydantic v2 para validación determinista, tipado estricto. |
| **API & Microservicios** | FastAPI & Uvicorn | Endpoints REST asíncronos, OpenAPI 3.1 auto-documentado, middlewares de seguridad y CORS. |
| **Orquestación de Agentes** | Agentic Frameworks (LangGraph, StateGraph, CrewAI o Gemini/LiteLLM SDK) | Agentes con memoria contextual, ejecución de herramientas tipadas y bucles de autocorrección. |
| **Base de Datos & Vector Store** | PostgreSQL + `pgvector` & Redis | Almacenamiento relacional transaccional + búsqueda híbrida (Vectorial densa + BM25) + caché de estados en Redis. |
| **Frontend & UI/UX** | HTML5 semántico + CSS3 Glassmorphic / Tailwind | Tokens de diseño, modo oscuro cuántico, tarjetas translúcidas, animaciones fluidas y accesibilidad WCAG 2.1 AA. |
| **Contenedores & Empaquetado** | Docker & OCI Containers | Multi-stage builds, ejecución sin privilegios de root (`appuser`), imágenes ultraligeras Alpine/Slim. |
| **Cloud & CI/CD** | GitHub Actions + GCP Cloud Run / AWS ECS / App Runner | Despliegue continuo serverless con escalado automático de 0 a N instancias. |

---

### 2. Arquitectura de Agente Inteligente & API Asíncrona (FastAPI + Pydantic v2)

```python
"""
Módulo de Servicio de Agente Inteligente (Cloud-Native AI-First)
"""
from typing import Annotated, Any, Dict, List, Optional
from fastapi import FastAPI, HTTPException, status, Depends
from pydantic import BaseModel, Field, ConfigDict
import asyncio

app = FastAPI(
    title="Intelligent Agent Core API",
    version="2.0.0",
    description="Microservicio asíncrono con arquitectura AI-First para orquestación de agentes autónomos."
)

class AgentQueryRequest(BaseModel):
    model_config = ConfigDict(strict=True)
    prompt: str = Field(..., min_length=2, max_length=4000, description="Consulta para el agente inteligente")
    session_id: str = Field(..., description="Identificador de sesión para memoria conversacional")
    metadata: Optional[Dict[str, Any]] = Field(default_factory=dict, description="Metadatos de contexto")

class AgentExecutionResult(BaseModel):
    agent_role: str
    response: str
    confidence_score: float = Field(ge=0.0, le=1.0)
    tools_executed: List[str]
    latency_ms: float

@app.get("/health", status_code=status.HTTP_200_OK)
async def health_check():
    """Healthcheck estándar para orquestadores en la nube (Cloud Run, AWS ECS, K8s)."""
    return {"status": "healthy", "service": "agent-core", "cloud_ready": True}

@app.post("/api/v1/agents/execute", response_model=AgentExecutionResult, status_code=status.HTTP_200_OK)
async def execute_agent_task(payload: AgentQueryRequest) -> AgentExecutionResult:
    # Simulación de orquestación asíncrona de agente
    await asyncio.sleep(0.05)
    return AgentExecutionResult(
        agent_role="nutrition-agent",
        response="Plan nutricional optimizado según requerimientos metabólicos del usuario.",
        confidence_score=0.98,
        tools_executed=["hybrid_search_bm25_pgvector", "dietary_calculator"],
        latency_ms=52.4
    )
```

---

### 3. Contenedorización Multi-Stage Segura (Dockerfile Cloud-Native)

Diseñado para desplegarse instantáneamente en **GCP Cloud Run**, **AWS App Runner**, **AWS ECS Fargate** o **Render/Railway**:

```dockerfile
# ==============================================================================
# Etapa 1: Builder
# ==============================================================================
FROM python:3.11-slim AS builder

WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# ==============================================================================
# Etapa 2: Runtime Seguro (Non-root user)
# ==============================================================================
FROM python:3.11-slim AS runtime

WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PORT=8080

RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq5 curl \
    && rm -rf /var/lib/apt/lists/* \
    && useradd --create-home --home-dir /home/appuser --shell /bin/bash appuser

COPY --from=builder /install /usr/local
COPY . /app

RUN chown -R appuser:appuser /app
USER appuser

EXPOSE 8080

HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:${PORT}/health || exit 1

CMD ["sh", "-c", "exec uvicorn src.main:app --host 0.0.0.0 --port ${PORT}"]
```

---

### 4. Automatización CI/CD Multi-Cloud desde GitHub Actions

Flujo estándar para desplegar automáticamente a **Google Cloud Platform (Cloud Run)** o **AWS**:

```yaml
name: Cloud-Native CI/CD Pipeline

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  test-and-validate:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Code
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"
          cache: "pip"

      - name: Install Dependencies
        run: |
          pip install --upgrade pip
          pip install -r requirements.txt
          pip install pytest flake8

      - name: Run Quality Linters
        run: flake8 . --count --max-line-length=120 --statistics

      - name: Run Test Suite
        run: pytest -v

  deploy-gcp-cloud-run:
    needs: test-and-validate
    if: github.ref == 'refs/heads/main' && github.event_name == 'push'
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Code
        uses: actions/checkout@v4

      - name: Google Cloud Auth
        uses: google-github-actions/auth@v2
        with:
          credentials_json: ${{ secrets.GCP_SA_KEY }}

      - name: Set up Cloud SDK
        uses: google-github-actions/setup-gcloud@v2

      - name: Build and Deploy to Cloud Run
        run: |
          gcloud builds submit --tag gcr.io/${{ secrets.GCP_PROJECT_ID }}/agent-service:${{ github.sha }}
          gcloud run deploy agent-service \
            --image gcr.io/${{ secrets.GCP_PROJECT_ID }}/agent-service:${{ github.sha }} \
            --platform managed \
            --region us-central1 \
            --allow-unauthenticated \
            --set-env-vars ENVIRONMENT=production
```

---

## 🔒 Estándares Universales de Seguridad (Ambos Arquetipos)

1. **Zero-Trust & Cero Secretos:** PROHIBIDO hardcodear credenciales, contraseñas, URLs de conexión o API keys en código fuente. Utilizar variables de entorno (`.env` local, GitHub Secrets en CI/CD, Cloud Secret Manager en producción).
2. **Defensa contra Inyecciones:**
   - En PHP: Sentencias preparadas con PDO obligatorias.
   - En Python: Validación estricta con Pydantic v2 y consultas parametrizadas con ORM o SQL Drivers seguros (`asyncpg`, `SQLAlchemy`).
3. **Protección XSS & CSRF:** Sanitización de salidas HTML y tokens anti-CSRF en toda operación mutante.
4. **Resiliencia de LLM y APIs:** Reintentos exponenciales con jitter en todas las llamadas a modelos o APIs externas.
