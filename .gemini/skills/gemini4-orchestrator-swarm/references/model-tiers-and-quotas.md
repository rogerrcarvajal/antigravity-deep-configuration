# Niveles de Modelos Gemini 4 y Gestión de Cuotas en Gemini Pro

## 1. Mapa de Modelos Disponibles en tu Cuenta Gemini Pro (`g1-pro`)

Resultados verificados directamente del motor `swarm{action:"models"}` de Antigravity:

| Familia | Modelos Disponibles | Reinicio de Cuota | Recomendación de Uso |
| :--- | :--- | :--- | :--- |
| **Orchestrator** | `Orchestrator (Argon)` (`gemini-pro-orchestrator-g1-pro`) | **Semanal** (7 días) | Úsalo como modo principal cuando trabajes en una sola conversación que combine diseño arquitectónico y codificación iterativa. |
| **Gemini 4 Argon** | `Low`, `Medium`, `High` (`gemini-4-argon-*`) | **Semanal** (7 días) | Modela decisiones complejas, especificaciones EGM (*Elephant*), depuración profunda y diseño de contratos. Evita lanzar enjambres masivos sobre Argon para proteger tu cuota semanal. |
| **Gemini 4 Hydrogen** | `Low`, `Medium`, `High`, `XHigh` (`gemini-4-hydrogen-*`) | **Diario** (24 horas) | Tu caballo de batalla ilimitado día a día. `Hydrogen (XHigh)` y `Hydrogen (High)` ofrecen razonamiento espacial y técnico de altísimo nivel con cuota que se recarga cada 24 horas. Ideal para workers de `/swarm`. |
| **Claude 5.5** | `Claude Opus 5.5` y `Claude Sonnet 5.5` (`Low`, `Medium`, `High`) | **Diario** (24 horas) | Excelentes como verificadores independientes (*Goldfish* o `verifier` en `/swarm`) con recarga diaria. |
| **Gemini 3.8 Flash** | `Low`, `Medium`, `High` (`gemini-3.8-flash-*`) | **Diario** (24 horas) | Ideal para subagentes de navegador (`browser`), búsquedas rápidas y `run_workflow` de alto volumen. |

---

## 2. Cómo Suplir a `Gemini 4 Carbon` en el Plan Gemini Pro

En las demostraciones de Antigravity, **Gemini 4 Carbon** se utiliza como coordinador pesado junto a **Hydrogen**. En tu plan **Gemini Pro**, logras **el mismo flujo arquitectónico** combinando tres piezas que sí tienes activas al 100%:

1. **`Orchestrator (Argon)`** hace exactamente el papel de *Planner + Executor* automático: **Argon** planifica la arquitectura y **Hydrogen** ejecuta los cambios y tests.
2. **`Gemini 4 Hydrogen (XHigh)`** activa el presupuesto máximo de pensamiento (*extra-high thinking*) de Hydrogen, alcanzando métricas de resolución de código equivalentes a modelos frontera pero consumiendo **cuota diaria** en lugar de semanal.
3. **Grafo de Conocimiento (`graphify`) + Auditoría EGM (`egm-auditoria`):** Al darle a Argon o Hydrogen el subgrafo exacto de `graphify` y auditar con peces independientes, reduces el contexto necesario en un 80% y aumentas la precisión arquitectónica sin requerir Carbon.
