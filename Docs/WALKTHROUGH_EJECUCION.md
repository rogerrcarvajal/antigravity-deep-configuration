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

## 4. Cómo Operar con Habilidades Autónomas (Agent Skills)

Las habilidades se activan automáticamente bajo demanda según la tarea requerida:

| Flujo de Trabajo | Habilidad Activada | Ejemplo de Disparador en Chat |
| :--- | :--- | :--- |
| **Onboarding / UI / Estándar de Stack** | `brand-identity` | *"Aplica la identidad de marca CEIA y diseña la vista de login con glassmorphism."* / *"Extrae el manual de identidad del proyecto X y genera tokens."* |
| **Generación de Changelog y Releases** | `changelog-generator` | *"Genera el changelog de los commits de los últimos 7 días categorizado para usuarios."* |
| **Creación y Benchmark de Nuevas Habilidades** | `skill-creator` | *"Crea una nueva habilidad para validar esquemas JSON y corre un benchmark con quick_validate.py."* |
| **Desarrollo Metódico de Sprints** | `sprint-issue-developer` | *"Desarrolla el Issue S1-02 siguiendo el bucle de desarrollo sin errores y abre un PR con Ref #12."* |

---

## 5. Gestión de la Documentación Viva
Para mantener viva la documentación:
- Cualquier nueva regla agregada en `.agents/rules/` debe ser respaldada en `Docs/`.
- Cualquier nuevo rol de agente debe añadirse a `.agents/agents/agents_registry.json` y reflejarse en este Walkthrough.
- Cualquier nueva habilidad incorporada debe ser documentada en `Docs/GUIA_HABILIDADES_AGENTICAS.md` e instalada tanto en `.agents/skills/` como en `~/.gemini/config/skills/`.

---

## 6. Pipeline de Integración Continua (CI/CD) y Validación Automatizada

El repositorio cuenta con una suite completa de pruebas e integración en GitHub Actions (`.github/workflows/ci.yml`):
- **Pruebas de Skills:** Verifica que todo `SKILL.md` cumpla con el estándar YAML frontmatter, longitud de descripción, formato kebab-case y estructura interna (`tests/test_skills.py`).
- **Pruebas de Configuración JSON:** Garantiza que los registros de agentes (`agents_registry.json`) y configuraciones MCP (`mcp_config.json`) sean JSON válidos y contengan los 5 roles canónicos (`tests/test_json_configs.py`).
- **Pruebas de Reglas y Documentación:** Verifica la integridad y contenido de las 6 reglas jerárquicas y documentación técnica (`tests/test_rules_structure.py`).
- **Comando de Ejecución Local:**
  ```bash
  pytest tests/ -v
  ```

