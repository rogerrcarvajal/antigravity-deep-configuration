---
name: egm-auditar
description: Ejecuta una auditoría independiente con el modelo Elephant-Goldfish (EGM) y los 4 peces revisores sin memoria.
---

# Workflow: egm-auditar

Sigue la skill `egm-auditoria` para ejecutar una auditoría independiente (Goldfish Review) sobre el archivo, especificación o aplicación indicada.

- Si se audita un diseño antes de programar: aplica el flujo **Elephant (planificación) → Goldfish (revisión independiente con `invoke_subagent`) → Decisión Humana**.
- Si se audita una web, app o entregable para cliente: lanza en paralelo los 4 peces (`cliente.md`, `desconfiado.md`, `proteccion-datos.md`, `tecnico.md`) en subagentes sin memoria previa (`research`) y genera `goldfish_review_report.md` en español.
