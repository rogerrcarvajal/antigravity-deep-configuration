---
trigger: model_decision
description: Optimiza el uso de Gemini 4 (Argon, Hydrogen, Orchestrator) y el despliegue de enjambres (/swarm y run_workflow) protegiendo la cuota semanal del plan Gemini Pro.
---

# Gobernanza de Gemini 4 Orchestrator & Swarm en Gemini Pro

1. **Selección Inteligente por Cuota (Semanal vs. Diaria):**
   - `Orchestrator (Argon)` y `Gemini 4 Argon` tienen **cuota semanal** (7 días): resérvalos para planificación arquitectónica, coordinación principal y decisiones críticas.
   - `Gemini 4 Hydrogen` (`Low`, `Medium`, `High`, `XHigh`), `Claude 5.5` y `Gemini 3.8 Flash` tienen **cuota diaria** (24 horas): úsalos para ejecución intensiva, pruebas, refactorizaciones masivas y workers de `/swarm`.
2. **Protocolo de Enjambre (`/swarm`):**
   - Antes de lanzar un `/swarm`, divide el trabajo en piezas sin colisión de archivos (1 archivo/módulo = 1 worker autor).
   - Asigna `workspace: "share"` a los autores que editan en paralelo y `workspace: "inherit"` a lectores y verificadores.
   - Incluye siempre **1 verificador por cada 2 a 4 autores** para revisar diffs y ejecutar tests antes de dar por cerrada una tarea.
   - Si un worker agota cuota, cámbialo en caliente con `swarm{action:"model", name, model}` sin usar `kill`.
   - Integra siempre los cambios de `workspace: "share"` o `"branch"` antes de ejecutar `kill` sobre un worker autor.
3. **Orquestación Programática (`run_workflow`):**
   - Para tareas repetitivas sobre listas de archivos o módulos que no requieren debate en tablero compartido, prefiere `run_workflow` con `parallel()` o `pipeline()`.
