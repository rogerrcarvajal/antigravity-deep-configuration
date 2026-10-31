# Walkthrough de Ejecución y Operación del Ecosistema Antigravity

> **Documento Vivo del Proyecto:** `c:\xampp\htdocs\antigravity-rules\Docs\WALKTHROUGH_EJECUCION.md`  
> **Propósito:** Guía práctica para operar el IDE y el modo de Administración de Agentes de Antigravity en el día a día bajo el enfoque Multi-Arquetipo (Core Web & Cloud-Native AI-First).

---

## 1. Validación de Conexión de GitHub MCP (En Vivo)
Se ha verificado la operatividad de GitHub MCP mediante llamadas en tiempo de ejecución:
- **Herramienta invocada:** `github:search_repositories` y `github:list_commits`
- **Resultado:** Respuesta exitosa con retorno de repositorios y confirmación del handshake con la API de GitHub.
- **Estado:** ✅ 100% Operativo y listo para crear ramas, issues y PRs.

---

## 2. Cómo Operar en el Modo IDE (Pair-Programming)

### Flujo de Desarrollo Recomendado:
1. **Comando `/plan`:**
   - Antes de pedir código para un nuevo módulo, escribe `/plan` seguido de tu requerimiento.
   - El agente asumirá el rol de **Arquitecto de Soluciones**, identificará el arquetipo aplicable (**Arquetipo A: Transaccional** o **Arquetipo B: Cloud-Native & AI-First**), creará un artefacto con diagramas Mermaid y contratos de API, y esperará tu aprobación antes de modificar archivos.
2. **Aplicación Automática de Reglas según Arquetipo:**
   - **Para proyectos existentes / Arquetipo A (ej. CEIA_SWGA):**
     * Al crear o editar `.php`, Antigravity aplica `30-backend-services.md` (Prepared Statements, PSR-12, formato JSON unificado, verificación de vulnerabilidad).
     * Cero regresiones ni cambios de paradigma forzados.
   - **Para nuevos proyectos / Arquetipo B (ej. Wellness Platform 2.0 / Nutrition Agent):**
     * Al crear o editar `.py`, aplica `20-python-ai-services.md` (FastAPI asíncrono, Pydantic v2 estricto, orquestación de agentes con StateGraph, RAG híbrido pgvector + BM25, healthcheck `/health`, variable `$PORT` y Dockerfile multi-stage).
   - **Para capas de Frontend (Ambos arquetipos):**
     * Aplica `40-frontend-uiux.md` (Tokens de diseño, modo oscuro, componentes glassmorphic y accesibilidad WCAG 2.1 AA).

---

## 3. Cómo Operar en el Modo Administración de Agentes (Multi-Agentes)

El archivo `.agents/agents/agents_registry.json` (y `.gemini/agents/agents_registry.json`) contiene la configuración de agentes especializados. Para utilizarlos en Antigravity:

### Invocación de Subagentes por Tarea:
| Tarea a Desarrollar | Agente Recomendado | Instrucción Tipo |
| :--- | :--- | :--- |
| **Diseño de Arquitectura & Selección de Arquetipo** | `solution-architect` | *"Diseña el modelo de entidades DDD, contratos OpenAPI y diagrama de flujo para el nuevo servicio de IA."* |
| **Microservicio de IA, Agentes Autónomos y RAG** | `python-ai-engineer` | *"Crea un microservicio FastAPI con un agente inteligente para recomendaciones nutricionales usando Pydantic v2 y pgvector."* |
| **API Transaccional en PHP/XAMPP (Arquetipo A)** | `backend-core-dev` | *"Implementa el endpoint POST /api/v1/students con validación PDO y manejo transaccional para SWGA."* |
| **Diseño de Interfaz de Usuario Glassmorphic** | `ui-ux-designer` | *"Crea el componente de chat del agente con diseño glassmorphic en modo oscuro y estados loading/empty."* |
| **Control de Calidad, Pentesting y Despliegue Cloud** | `qa-security-auditor` | *"Audita el código contra OWASP, valida el Dockerfile y crea un Pull Request hacia main con GitHub MCP para disparar el despliegue en GCP Cloud Run."* |

---

## 4. Cómo Operar con Habilidades Autónomas (Agent Skills)

Las habilidades se activan automáticamente bajo demanda según la tarea requerida:

| Flujo de Trabajo | Habilidad Activada | Ejemplo de Disparador en Chat |
| :--- | :--- | :--- |
| **Onboarding / UI / Estándar Multi-Arquetipo** | `brand-identity` | *"Aplica la identidad de marca de Rogerr Carvajal con arquetipo Cloud-Native y prepara el microservicio para GCP."* / *"Diseña la vista SWGA con la paleta CEIA."* |
| **Generación de Changelog y Releases** | `changelog-generator` | *"Genera el changelog de los commits de los últimos 7 días categorizado para usuarios."* |
| **Creación y Benchmark de Nuevas Habilidades** | `skill-creator` | *"Crea una nueva habilidad para validar despliegues en AWS ECS y corre el benchmark con quick_validate.py."* |
| **Desarrollo Metódico de Sprints** | `sprint-issue-developer` | *"Desarrolla el Issue S2-01 de Wellness Platform 2.0 en bucle sin errores y abre un PR con Ref #33."* |

---

## 5. Estrategia de Despliegue Multi-Cloud desde GitHub (GCP, AWS)

Para proyectos del **Arquetipo B (Cloud-Native AI-First)**, el flujo de entrega continua está desacoplado de la infraestructura local:
1. **GitHub MCP:** El agente `qa-security-auditor` valida las pruebas locales (`pytest`), hace commit bajo Conventional Commits y crea el Pull Request con `Ref #X`.
2. **GitHub Actions CI:** Ejecuta automáticamente linters y suites de pruebas en Ubuntu Runner.
3. **Despliegue Serverless Automatizado:**
   - **Google Cloud Platform (GCP):** Construye la imagen OCI y la despliega a **Cloud Run** con escalado automático de 0 a N instancias.
   - **Amazon Web Services (AWS):** Publica en Amazon ECR y actualiza **AWS App Runner** o **AWS ECS Fargate**.
   - **Variables de Entorno:** Se inyectan de forma segura desde GitHub Secrets o Secret Manager, sin credenciales en el repositorio.

---

## 6. Pipeline de Integración Continua (CI/CD) y Validación Automatizada

El repositorio cuenta con una suite completa de pruebas en GitHub Actions (`.github/workflows/ci.yml`):
- **Pruebas de Skills:** Verifica que todo `SKILL.md` cumpla con el estándar YAML frontmatter, longitud de descripción, formato kebab-case y estructura interna (`tests/test_skills.py`).
- **Pruebas de Configuración JSON:** Garantiza que los registros de agentes (`agents_registry.json`) y configuraciones MCP (`mcp_config.json`) sean JSON válidos y contengan los 5 roles canónicos (`tests/test_json_configs.py`).
- **Pruebas de Reglas y Documentación:** Verifica la integridad y contenido de las 6 reglas jerárquicas y documentación técnica (`tests/test_rules_structure.py`).
- **Comando de Ejecución Local:**
  ```bash
  python -m pytest tests/ -v
  ```

---

## 7. Operación del Autonomous Agent Execution Loop
Para ejecutar tareas con el bucle autónomo sin errores:
1. Consultar la guía [`Docs/SELECCION_SKILLS_Y_AGENT_LOOP.md`](./SELECCION_SKILLS_Y_AGENT_LOOP.md).
2. Utilizar el prompt estandarizado con backpressure y looping silencioso para que el agente resuelva fallos internamente antes de emitir su reporte.
3. Certificar que el checklist de verificación empírica esté completo antes de autorizar el merge en GitHub.

