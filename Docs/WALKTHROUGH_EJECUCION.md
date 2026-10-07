# Walkthrough de Ejecución y Operación del Ecosistema Antigravity

> **Documento Vivo del Proyecto:** `c:\xampp\htdocs\antigravity-rules\Docs\WALKTHROUGH_EJECUCION.md`  
> **Propósito:** Guía práctica para operar el IDE y el modo de Administración de Agentes de Antigravity en el día a día.

---

## 1. Validación de Conexión de GitHub MCP (En Vivo)
Se ha verificado la operatividad de GitHub MCP mediante llamadas en tiempo de ejecución:
- **Herramienta invocada:** `github:search_repositories`
- **Resultado:** Respuesta exitosa con retorno de repositorios y confirmación del handshake con la API de GitHub.
- **Estado:** ✅ 100% Operativo y listo para crear ramas, issues y PRs.

---

## 2. Cómo Operar en el Modo IDE (Pair-Programming)

### Flujo de Desarrollo Recomendado:
1. **Comando `/plan`:**
   - Antes de pedir código para un nuevo módulo, escribe `/plan` seguido de tu requerimiento.
   - El agente asumirá el rol de **Arquitecto de Soluciones**, creará un artefacto con diagramas Mermaid y contratos de API, y esperará tu aprobación antes de modificar archivos.
2. **Aplicación Automática de Reglas:**
   - Si creas o modificas un archivo `.py`, Antigravity aplicará automáticamente `20-python-ai-services.md` (Pydantic, `async def`, `uv`).
   - Si creas o modificas un archivo `.php`, aplicará `30-backend-services.md` (Prepared Statements, PSR-12, formato JSON unificado).
   - Si trabajas en vistas o frontend, aplicará `40-frontend-uiux.md` (Accesibilidad WCAG, Tailwind tokens, estados de componente).

---

## 3. Cómo Operar en el Modo Administración de Agentes (Multi-Agentes)

El archivo `.gemini/agents/agents_registry.json` contiene la configuración de agentes especializados. Para utilizarlos en Antigravity:

### Invocación de Subagentes por Tarea:
| Tarea a Desarrollar | Agente Recomendado | Instrucción Tipo |
| :--- | :--- | :--- |
| **Diseño del Sistema / Base de Datos** | `solution-architect` | *"Diseña el modelo de entidades DDD y diagrama de flujo para el módulo de facturación."* |
| **Microservicio de IA o Procesamiento** | `python-ai-engineer` | *"Crea un microservicio FastAPI para procesar documentos y generar embeddings con Pydantic v2."* |
| **API Transaccional en PHP/XAMPP** | `backend-core-dev` | *"Implementa el endpoint POST /api/v1/orders con validación PDO y manejo transaccional."* |
| **Diseño de Interfaz de Usuario** | `ui-ux-designer` | *"Crea la vista de dashboard con Tailwind CSS implementando estados loading, empty y error."* |
| **Control de Calidad y Pull Request** | `qa-security-auditor` | *"Audita el código contra OWASP, ejecuta tests y crea un Pull Request hacia la rama main con GitHub MCP."* |

---

## 4. Gestión de la Documentación Viva
Para mantener viva la documentación:
- Cualquier nueva regla agregada en `.gemini/rules/` debe ser respaldada en `Docs/`.
- Cualquier nuevo rol de agente debe añadirse a `.gemini/agents/agents_registry.json` y reflejarse en este Walkthrough.
