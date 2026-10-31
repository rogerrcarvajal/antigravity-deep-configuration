# 20 - Directrices para Microservicios de Python, Agentes Inteligentes e IA Cloud-Native

Aplica a cualquier archivo bajo directorios `python_services/`, `src/`, `ai/`, `agents/`, `scripts/` o con extensión `.py`.

---

## 1. Gestión del Entorno, Paquetes y Runtime
- **Runtime:** Python 3.11+ o 3.12+. Utilizar sintaxis moderna de tipado (`str | None` en lugar de `Optional[str]`).
- **Gestión de Paquetes:** Priorizar `uv` o `poetry` para una resolución de dependencias determinista y ultrarrápida. Archivo `requirements.txt` o `pyproject.toml` versionado.

---

## 2. Paradigma Asíncrono y Validación Estricta con Pydantic v2
- **Async-First:** Toda operación con operaciones I/O intensivas (endpoints de API, consultas SQL, llamadas a LLMs o bases vectoriales) debe ser declarada como `async def` utilizando clientes asíncronos (`httpx`, `asyncpg`, `aiofiles`).
- **Pydantic v2:**
  - Todo payload de entrada y respuesta de endpoint debe modelarse con `pydantic.BaseModel`.
  - Habilitar `model_config = ConfigDict(strict=True)` para datos críticos o de validación de herramientas.

---

## 3. Buenas Prácticas para Desarrollo con Enfoque de Agentes Inteligentes
- **Orquestación y Grafos de Estado:**
  - Estructurar agentes como máquinas de estado o grafos dirigidos (patrón StateGraph / LangGraph / ReAct).
  - Separar claramente la planificación (Planner), ejecución de herramientas (Tool Execution) y síntesis/crítica (Evaluator/Critic).
- **Tool Calling Tipado:**
  - Cada herramienta (tool) expuesta a un agente debe contar con docstring detallado y esquema Pydantic para sus argumentos.
  - Validar siempre los argumentos de las herramientas antes de su ejecución.
- **Memoria Contextual:**
  - Memoria a corto plazo (ventana de conversación): gestionar en memoria o Redis.
  - Memoria a largo plazo / RAG: búsqueda híbrida combinando similitud densa vectorial (`pgvector`) con búsqueda léxica (BM25) y fusión recíproca de rangos (RRF).
- **Límites de Recursión y Resiliencia:**
  - Definir `max_iterations` y timeouts en todo bucle agentico para evitar loops infinitos.
  - Implementar reintentos exponenciales con jitter (`tenacity`) para mitigar rate limits de LLMs.

---

## 4. Estándares Cloud-Native y Despliegue en Contenedores (GCP, AWS)
- **12-Factor App:** Configuración 100% inyectada vía variables de entorno (`.env` local, Secret Manager en nube).
- **Puerto Dinámico:** Escuchar obligatoriamente en `${PORT:-8080}` para compatibilidad nativa con **Google Cloud Run**, **AWS App Runner** y **AWS ECS**.
- **Healthcheck Endpoint:** Implementar `/health` para chequeos de vivacidad (Liveness) y `/ready` para preparación (Readiness).
- **Dockerfile Multi-Stage:**
  - Compilación de dependencias en etapa builder.
  - Runtime limpio ejecutado con usuario no root (`appuser`).
  - `.dockerignore` estricto excluyendo `.git`, `.env`, `__pycache__` y carpetas de pruebas.
