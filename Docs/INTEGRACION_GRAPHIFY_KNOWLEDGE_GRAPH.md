# Integración de Graphify Knowledge Graph en Google Antigravity

## 1. Resumen Ejecutivo y Objetivo

**Graphify** (`Graphify-Labs/graphify` / `safishamsi/graphify`) es un motor de análisis estructural y grafos de conocimiento diseñado para asistentes de codificación con IA. Su propósito central es **reducir drásticamente el consumo de tokens (hasta un 80%)** durante el desarrollo y análisis de código en repositorios medianos y grandes.

En lugar de cargar decenas de archivos completos en el contexto del LLM o hacer barridos ciegos con `grep`, Antigravity consulta un **grafo de conocimiento local indexado** mediante Tree-sitter AST (sin costo de API ni consumo de tokens durante la extracción de código).

```
┌────────────────────────────────────────────────────────┐
│               Código Fuente / Documentos               │
└───────────────────────────┬────────────────────────────┘
                            │
                            ▼
              ┌───────────────────────────┐
              │    Extracción AST Local   │  (Tree-sitter, $0 tokens)
              │    Detección Comunidades  │
              └─────────────┬─────────────┘
                            │
                            ▼
       ┌────────────────────┴────────────────────┐
       ▼                                         ▼
┌─────────────────────────┐           ┌─────────────────────────┐
│  graphify-out/graph.json│           │ graphify-out/graph.html │
│  (GraphRAG Queryable)   │           │ (Visualización 3D/2D)   │
└────────────┬────────────┘           └─────────────────────────┘
             │
             ▼
┌────────────────────────────────────────────────────────┐
│              Google Antigravity Agent                  │
│   Consulta subgrafos focalizados (Query / Path / Node)  │
│             Ahorro de hasta un 80% en tokens           │
└────────────────────────────────────────────────────────┘
```

---

## 2. Componentes Integrados en Antigravity

La integración se implementó en capas multinivel en el espacio de trabajo local y en la configuración global de Google Antigravity:

| Componente | Ubicación Local (.agents / .gemini) | Ubicación Global Antigravity | Función |
| :--- | :--- | :--- | :--- |
| **Skill Principal** | `.agents/skills/graphify/SKILL.md`<br>`.gemini/skills/graphify/SKILL.md` | `~/.gemini/config/skills/graphify/SKILL.md` | Habilidad interactiva `/graphify` para indexar, consultar y actualizar grafos. |
| **Referencias** | `.agents/skills/graphify/references/` | `~/.gemini/config/skills/graphify/references/` | Módulos de referencia rápida (`query.md`, `update.md`, `exports.md`, etc.). |
| **Regla Always-On** | `.agents/rules/graphify.md`<br>`.gemini/rules/graphify.md` | `~/.gemini/config/rules/graphify.md` | Fuerza a Antigravity a consultar el grafo antes de leer archivos en bloque. |
| **Workflow** | `.agents/workflows/graphify.md`<br>`.gemini/workflows/graphify.md` | - | Flujo de ejecución `/graphify` registrado en el pipeline del agente. |
| **MCP Server** | `.agents/mcp_config.json`<br>`.gemini/mcp_config.json` | `~/.gemini/config/mcp_config.json` | Conector stdio MCP `graphify.serve` para navegación por herramientas semánticas. |

---

## 3. Comandos de Uso

### 3.1. Construcción del Grafo

```powershell
# Indexar el proyecto actual (genera HTML interactivo y graph.json)
/graphify .

# Indexar con generación de wiki documental navegable
/graphify . --wiki

# Actualización incremental tras modificar código (AST local, instantáneo y gratuito)
graphify update .
```

### 3.2. Consultas Semánticas (Ahorro de Tokens)

```powershell
# Búsqueda semántica por BFS (recorre el contexto relevante)
graphify query "¿Cómo interactúa la autenticación con la base de datos?"

# Búsqueda por profundidad DFS (traza un flujo específico)
graphify query "Flujo de registro de usuario" --dfs

# Limitar presupuesto de tokens estricto
graphify query "¿Qué hace el servicio de IA?" --budget 1000

# Encontrar la ruta más corta entre dos componentes o módulos
graphify path "AuthService" "DatabasePool"

# Explicación focalizada de un nodo o clase
graphify explain "AgentOrchestrator"
```

---

## 4. Archivos de Salida Generados (`graphify-out/`)

- `graphify-out/graph.json`: Estructura GraphRAG con nodos (archivos, clases, funciones), aristas (`CALLS`, `IMPORTS`, `INFERRED`) y comunidades temáticas.
- `graphify-out/graph.html`: Visualizador interactivo para explorar el árbol de arquitectura en el navegador.
- `graphify-out/GRAPH_REPORT.md`: Informe ejecutivo con god nodes, modularidad y métricas de acoplamiento.
- `graphify-out/wiki/index.md`: Wiki navegable estructurada por comunidades funcionales para que los agentes la lean antes de explorar el código crudo.

---

## 5. Regla Activa de Antigravity (`rules/graphify.md`)

```markdown
---
trigger: always_on
description: Consult the graphify knowledge graph at graphify-out/ for codebase and architecture questions.
---

## graphify

This project has a graphify knowledge graph at graphify-out/.

Rules:
- For codebase or architecture questions, when `graphify-out/graph.json` exists, first run `graphify query "<question>"` (CLI) or `query_graph` (MCP). Use `graphify path "<A>" "<B>"` / `shortest_path` for relationships and `graphify explain "<concept>"` / `get_node` for focused concepts.
- If graphify-out/wiki/index.md exists, navigate it instead of reading raw files.
- Read graphify-out/GRAPH_REPORT.md only for broad architecture review or when query/path/explain do not surface enough context.
- After modifying code files in this session, run `graphify update .` to keep the graph current (AST-only, no API cost).
```

---

## 6. Sinergia con REA y el Agent Loop

1. **Ingeniería Inversa (REA):** Al deconstruir un sistema binario o repositorio legado, `graphify` genera el mapa estructural de dependencias en segundos, permitiendo al agente saber con precisión qué módulos atacar primero.
2. **Agent Loop (Plan-Validate-Execute):** Durante la fase de análisis del ciclo de sprint, el agente extrae únicamente el subgrafo relevante del requerimiento, reduciendo el ruido de contexto y maximizando la precisión en las decisiones arquitectónicas.
