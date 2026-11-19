---
trigger: model_decision
description: Optimiza el uso de Gemini 4 (Neon, Argon, Hydrogen y Orchestrator Neon/Argon) y el despliegue de enjambres (/swarm y run_workflow) maximizando la ventana de 1M de tokens y la cuota diaria en Gemini Pro.
---

# Gobernanza de Gemini 4 (Neon / Argon / Hydrogen) Orchestrator & Swarm en Gemini Pro

1. **Prioridad de Modelos por Cuota y Capacidad (Neon como Motor Principal):**
   - **`Orchestrator (Neon)`** (`gemini-pro-orchestrator-neon`) y **`Gemini 4 Neon`** (`Low`, `Medium`, `High`, `XHigh`) cuentan con **ventana de contexto unificada de 1 millón de tokens (entrada/salida)**, velocidad **3x superior a Carbon** y **reinicio de cuota diario (24 horas)**. Son la elección principal por defecto para programación compleja, coordinación de `/swarm` y procesamiento de contextos grandes.
   - **`Gemini 4 Hydrogen`** (`Low`, `Medium`, `High`, `XHigh`), **`Claude 5.5`** y **`Gemini 3.8 Flash`** también tienen **cuota diaria (24 horas)**: úsalos para ejecución paralela rápida, UI, pruebas y verificación cruzada en `/swarm`.
   - **`Orchestrator (Argon)`** y **`Gemini 4 Argon`** tienen **cuota semanal (7 días)**: resérvalos como segunda opinión arquitectónica profunda o respaldo (*failover*) cuando la cuota diaria de Neon se agote.
2. **Protocolo de Enjambre (`/swarm` y `/swarm-pro`):**
   - Antes de lanzar un `/swarm`, divide el trabajo sin colisión de archivos (1 archivo/módulo = 1 worker autor).
   - Asigna `workspace: "share"` a los autores que editan en paralelo y `workspace: "inherit"` a lectores y verificadores.
   - Combina workers `gemini-4-neon-high` / `gemini-4-neon-medium` (para lógica compleja y contexto amplio de 1M tokens) con `gemini-4-hydrogen-high` (para subtareas rápidas).
   - Incluye siempre **1 verificador por cada 2 a 4 autores** para revisar diffs y ejecutar tests antes de cerrar una tarea.
   - Si un worker agota cuota, cámbialo en caliente con `swarm{action:"model", name, model}` sin usar `kill`.
   - Integra siempre los cambios de `workspace: "share"` o `"branch"` antes de ejecutar `kill` sobre un worker autor.
3. **Orquestación Programática (`run_workflow`):**
   - Para tareas repetitivas sobre listas de archivos o módulos que no requieren debate en tablero compartido, prefiere `run_workflow` con `parallel()` o `pipeline()`.
