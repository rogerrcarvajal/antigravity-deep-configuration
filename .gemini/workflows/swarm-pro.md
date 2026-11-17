---
name: swarm-pro
description: Despliega un enjambre coordinado (/swarm) o flujo paralelo optimizado para el plan Gemini Pro usando la skill gemini4-orchestrator-swarm.
---

# Workflow: swarm-pro

Sigue la skill `gemini4-orchestrator-swarm` (y la skill interna `swarm`) para estructurar y lanzar un equipo de agentes en paralelo:

1. **Verifica cuotas y modelos** con `swarm{action:"models"}`.
2. **Divide la tarea sin colisiones de archivos:** define qué archivos posee cada worker autor (`workspace: "share"`) y añade al menos un `verifier` (`workspace: "inherit"`).
3. **Nombra el swarm** con `swarm{action:"title"}` y lanza los workers con briefs autocontenidos.
4. **Muestra el enlace `open_board`** al usuario al final del turno de creación y coordina mediante `swarm_wait` y `read_board`.
