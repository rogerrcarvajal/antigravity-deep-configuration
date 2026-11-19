# Niveles de Modelos Gemini 4 (Neon, Argon, Hydrogen) y Gestión de Cuotas en Gemini Pro

## 1. Inventario Completo Verificado en tu Cuenta Gemini Pro (`swarm{action:"models", all:true}`)

| Familia | Modelos Disponibles en tu Selector | Reinicio de Cuota | Ventana y Características | Recomendación Estratégica |
| :--- | :--- | :--- | :--- | :--- |
| **Orchestrator (Neon)** ⭐ | `Orchestrator (Neon)` (`gemini-pro-orchestrator-neon`) | **Diario (24 horas)** | **1M tokens unificados (In/Out)** · Coordinación dinámica Neon + Hydrogen | **Tu nuevo modo por defecto para casi todo.** Combina el cerebro de programación de Neon con la velocidad de Hydrogen y se recarga cada 24h. |
| **Gemini 4 Neon** ⭐ | `Low`, `Medium`, `High`, `XHigh` (`gemini-4-neon-*`) | **Diario (24 horas)** | **1M tokens unificados**, hasta 3x más rápido que Carbon, optimizado en coste/tarea | Ideal para programación compleja, refactorizaciones grandes, análisis de repositorios enteros y workers principales de `/swarm`. |
| **Gemini 4 Hydrogen** | `Low`, `Medium`, `High`, `XHigh` (`gemini-4-hydrogen-*`) | **Diario (24 horas)** | Alta velocidad, eficiencia y razonamiento espacial | Excelente para workers paralelos de ejecución rápida, generación de UI, tests y subtareas en `/swarm`. |
| **Orchestrator (Argon)** | `Orchestrator (Argon)` (`gemini-pro-orchestrator-g1-pro`) | **Semanal (7 días)** | Coordinación Argon + Hydrogen | Úsalo como reserva estratégica cuando busques el estilo de razonamiento de Argon o si agotaste la cuota diaria de Neon. |
| **Gemini 4 Argon** | `Low`, `Medium`, `High` (`gemini-4-argon-*`) | **Semanal (7 días)** | Razonamiento profundo de largo horizonte | Resérvalo para decisiones arquitectónicas puntuales (*Elephant*) para no agotar su cuota semanal en tareas repetitivas. |
| **Claude 5.5** | `Claude Opus 5.5` y `Claude Sonnet 5.5` (`Low`, `Medium`, `High`) | **Diario (24 horas)** | Diversidad de familia de modelo | Perfectos como revisores independientes (*Goldfish* o `verifier` en `/swarm`). |
| **Gemini 3.8 Flash** | `Low`, `Medium`, `High` (`gemini-3.8-flash-*`) | **Diario (24 horas)** | Latencia mínima | Subagentes de navegador (`browser`) y `run_workflow` masivos. |

---

## 2. Gemini 4 Neon vs. Carbon, Argon y Hydrogen

Según la arquitectura oficial de la familia Gemini 4:

- **Posicionamiento:** **Gemini 4 Neon** se sitúa como el punto de equilibrio óptimo entre *Hydrogen* y *Carbon*: ofrece inteligencia de programación de nivel frontera a **3 veces la velocidad de Carbon** y una fracción del coste por tarea.
- **Ventana de Contexto Unificada de 1 Millón de Tokens:** Tanto la entrada como la salida comparten el pool de 1M de tokens, lo que evita cuellos de botella al generar archivos largos o analizar múltiples módulos simultáneamente.
- **Ventaja en Gemini Pro:** Al contar con **reinicio de cuota diario (cada 24 horas)** tanto en `Gemini 4 Neon (Low/Medium/High/XHigh)` como en `Orchestrator (Neon)`, puedes ejecutar sesiones intensivas de programación y enjambres `/swarm` todos los días sin temor a consumir el presupuesto semanal de Argon.

---

## 3. Estrategia de Escalado y Failover de Cuotas

1. **Nivel Primario (Uso Diario Intensivo):** `Orchestrator (Neon)` o `Gemini 4 Neon (Medium / High / XHigh)`.
2. **Nivel de Ejecución Masiva en Paralelo (`/swarm` workers):** Combinación de `gemini-4-neon-medium` / `gemini-4-neon-high` (módulos complejos) + `gemini-4-hydrogen-high` (módulos rápidos).
3. **Nivel de Reserva (Failover):** Si en una jornada extrema se alcanza el límite diario de Neon, cambia en caliente con `swarm{action:"model", model:"gemini-4-hydrogen-xhigh"}` (cuota diaria independiente) o a `Orchestrator (Argon)` / `gemini-4-argon-medium` (reserva semanal).
