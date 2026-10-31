# 10 - Arquitectura del Workspace y Ecosistema Multi-Arquetipo de Alto Impacto

Este documento define la arquitectura técnica del entorno de Antigravity para soportar desarrollo de software de vanguardia bajo un enfoque **Multi-Arquetipo Adaptativo**.

Permite que convivan armónicamente:
1. **Sistemas Transaccionales Core Web Existentes** (Línea Base CEIA / SWGA).
2. **Nuevos Desarrollos Cloud-Native con Enfoque de Agentes Inteligentes** (Línea Base Wellness Platform 2.0 / Nutrition Agent).

---

## 1. Matriz de Arquetipos de Desarrollo

| Dimensión | Arquetipo A: Core Web Transaccional (CEIA / SWGA) | Arquetipo B: Cloud-Native & AI-First (Wellness 2.0) |
| :--- | :--- | :--- |
| **Enfoque de Negocio** | Gestión académica, ERP, plataformas transaccionales. | Asistentes inteligentes, sistemas RAG, agentes autónomos, analítica de IA. |
| **Backend & Core** | PHP 8.2+ POO / MVC / PSR-4, 7, 12, 15. | Python 3.11+ / 3.12+, FastAPI asíncrono (`async def`), Pydantic v2. |
| **Inteligencia Artificial** | Integraciones periféricas vía APIs REST / MCP. | Agentes autónomos nativos, StateGraphs (LangGraph), Tool Use tipado, RAG Híbrido. |
| **Persistencia** | PostgreSQL 14+ / MariaDB con PDO Prepared Statements. | PostgreSQL + `pgvector` (búsqueda densa) + BM25 (búsqueda léxica) + Redis (estados). |
| **Frontend & UI** | HTML5 semántico, CSS3 Vanilla, JavaScript nativo. | HTML5 semántico, CSS3 Glassmorphic / Tailwind tokens, JavaScript reactivo. |
| **Despliegue & Nube** | Apache / Nginx (XAMPP local), VPS, Servidor Dedicado. | **Cloud-Native OCI Container (Docker multi-stage)**, serverless container desplegable desde GitHub a **GCP Cloud Run**, **AWS ECS / App Runner**, Azure o PaaS. |

---

## 2. Detección Automática y No Afectación de Proyectos Existentes

> [!IMPORTANT]
> **Garantía de Compatibilidad Retrospectiva:**
> Los proyectos actualmente desarrollados bajo el Arquetipo A (como CEIA_SWGA) no son alterados ni forzados a migrar. Antigravity detecta el contexto del proyecto por sus archivos fuente:
> - Si detecta `composer.json`, `index.php` o rutas PHP: aplica estrictamente los estándares del **Arquetipo A**.
> - Si detecta `requirements.txt`, `pyproject.toml`, FastAPI o agentes Python: activa los estándares del **Arquetipo B**.
> - En proyectos políglotas híbridos: cada subsistema se rige por su respectivo arquetipo, comunicándose mediante contratos OpenAPI 3.1.

---

## 3. Patrón Arquitectónico Base: Hexagonal / DDD

Ambos arquetipos implementan el patrón **Ports & Adapters (Arquitectura Hexagonal)** con **Domain-Driven Design (DDD)** para garantizar desacoplamiento total:

```text
src/
├── core/
│   ├── domain/           # Entidades, Value Objects, Excepciones de Dominio (Cero dependencias)
│   │   └── models/
│   └── application/      # Casos de uso, DTOs, Puertos / Interfaces de repositorios y agentes
│       ├── use_cases/
│       └── ports/
└── infrastructure/       # Adaptadores de Entrada y Salida
    ├── http/             # Controladores (PHP) o Rutas FastAPI (Python), Middlewares
    ├── persistence/      # Repositorios PDO / SQL / pgvector, Modelos ORM
    └── external_services/# Clientes de APIs de LLMs, MCPs, pasarelas de pago
```

---

## 4. Flujo de Trabajo Obligatorio (Development Workflow)

1. **Fase 1: Planificación Formal (`/plan`):**
   - Análisis de requerimientos, definición del arquetipo (A o B), diagramas de arquitectura en Mermaid y modelo de entidades antes de codificar.
2. **Fase 2: Contratos de Interfaz (API-First):**
   - Especificaciones OpenAPI 3.1 o JSON Schema validadas antes de acoplar frontend y backend.
3. **Fase 3: Bucle de Desarrollo Guiado por Pruebas (TDD & Looping):**
   - Ciclos de desarrollo en bucle hasta alcanzar 0 errores (`pytest` para Python, `phpunit` para PHP).
4. **Fase 4: Empaquetado Cloud & Verificación con GitHub MCP:**
   - Si es Arquetipo B: validación de Dockerfile multi-stage, healthcheck `/health` y pipeline de GitHub Actions hacia GCP/AWS.
   - Apertura y gestión de Pull Requests mediante GitHub MCP con trazabilidad `Ref #X`.
