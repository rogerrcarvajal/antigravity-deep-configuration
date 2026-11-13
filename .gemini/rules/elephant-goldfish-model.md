---
trigger: model_decision
description: Aplica la estrategia Elephant-Goldfish Model (EGM) para auditar diseños, especificaciones o apps antes de codificar o entregar a cliente.
---

# Estrategia de Auditoría Elephant-Goldfish Model (EGM)

Para evitar el sesgo de confirmación y detectar supuestos ocultos antes de escribir código o entregar a producción:

1. **Rol Elephant (Sesión Principal):**
   - Comprende los requisitos, el contexto del negocio y la arquitectura existente.
   - Redacta el brief (`concepts_brief.md`) o borrador técnico (`design_draft.md`) antes de codificar módulos complejos.
2. **Rol Goldfish (Subagentes Independientes Sin Memoria):**
   - Antes de implementar un diseño crítico o entregar una app al cliente, lanza subagentes aislados (`invoke_subagent`) **sin pasarles el historial de la conversación**.
   - Cada Goldfish evalúa únicamente el artefacto escrito + el contexto real del negocio/código y reporta hallazgos clasificados en 🔴 Bloqueantes, 🟡 Importantes y 🟢 Detalles.
3. **Human-in-the-Loop:**
   - El agente nunca auto-aprueba ni corrige en silencio hallazgos de arquitectura o negocio: presenta el informe y permite que el desarrollador decida qué ajustar.
4. **Recursos Disponibles Globalmente:**
   - Plugin oficial EGM: `~/.gemini/config/plugins/egm/` (`/egm-brainstorm`, `/egm-draft`, `/egm-review`, `/egm-review-loop`, `/egm-resolve`, `/egm-bootstrap`, `/egm-drift-report`).
   - Skill de Auditoría en Español (Kit EGM): `~/.gemini/config/skills/egm-auditoria/` (con los 4 peces y plantillas de contexto).
