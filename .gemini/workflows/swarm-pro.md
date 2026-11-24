---
name: swarm-pro
description: Despliega un enjambre coordinado (/swarm) con la tríada Gemini 4 (Carbon para arquitectura/verificación, Neon para módulos 1M tokens e Hydrogen para ejecución rápida) usando gemini4-orchestrator-swarm.
---

# Workflow: swarm-pro

Sigue la skill `gemini4-orchestrator-swarm` (y la skill interna `swarm`) para estructurar y lanzar un equipo de agentes en paralelo aprovechando la tríada completa **Gemini 4 Carbon + Neon + Hydrogen**:

1. **Verifica cuotas y modelos vigentes** con `swarm{action:"models"}` (evitando modelos *Leaving Soon* como `Argon` y `3.8 Flash`).
2. **Divide la tarea sin colisiones de archivos:** asigna módulos críticos a `gemini-4-carbon-*` o `gemini-4-neon-high`, ejecución rápida/UI/tests a `gemini-4-hydrogen-high` (`workspace: "share"`), y al menos un `verifier` (`workspace: "inherit"`).
3. **Nombra el swarm** con `swarm{action:"title"}` y lanza los workers con briefs autocontenidos.
4. **Muestra el enlace `open_board`** al usuario al final del turno de creación y coordina mediante `swarm_wait` y `read_board`.
