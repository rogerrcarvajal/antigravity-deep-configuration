---
name: swarm-pro
description: Despliega un enjambre coordinado (/swarm) o flujo paralelo optimizado con Gemini 4 Neon (1M tokens, cuota diaria) y Hydrogen usando la skill gemini4-orchestrator-swarm.
---

# Workflow: swarm-pro

Sigue la skill `gemini4-orchestrator-swarm` (y la skill interna `swarm`) para estructurar y lanzar un equipo de agentes en paralelo aprovechando **Gemini 4 Neon** y **Hydrogen**:

1. **Verifica cuotas y modelos** con `swarm{action:"models"}` (priorizando `gemini-4-neon-*` y `gemini-4-hydrogen-*` con reinicio diario de 24h frente a la cuota semanal de Argon).
2. **Divide la tarea sin colisiones de archivos:** define qué archivos posee cada worker autor (`workspace: "share"`) y añade al menos un `verifier` (`workspace: "inherit"`).
3. **Nombra el swarm** con `swarm{action:"title"}` y lanza los workers con briefs autocontenidos.
4. **Muestra el enlace `open_board`** al usuario al final del turno de creación y coordina mediante `swarm_wait` y `read_board`.
