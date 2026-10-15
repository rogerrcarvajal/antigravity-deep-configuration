---
name: "Reporte de Fallo / Bug Report"
about: Reporta una inconsistencia, error en reglas, skills o configuración de Antigravity
title: "[BUG] <descripción breve del fallo>"
labels: ["bug", "triage"]
assignees: ["rogerrcarvajal"]
---

### 📌 Descripción del Fallo
Describe de manera concisa y clara el comportamiento erróneo observado.

### 🧩 Componente Afectado
- [ ] Regla Contextual (`.agents/rules/` o `.gemini/rules/`)
- [ ] Habilidad Agéntica (`brand-identity`, `changelog-generator`, `skill-creator`, `sprint-issue-developer`)
- [ ] Agente Especializado (`solution-architect`, `python-ai-engineer`, `backend-core-dev`, etc.)
- [ ] Integración GitHub MCP Server
- [ ] Workflow CI / GitHub Actions

### 🔁 Pasos para Reproducir
1. Ejecutar comando / invocar agente con: `...`
2. Abrir archivo: `...`
3. Ver el resultado o mensaje de error: `...`

### 📉 Comportamiento Observado vs Esperado
- **Observado:** 
- **Esperado:** 

### 🪵 Logs y Trazas de Error
```text
(Pega aquí las trazas de consola, output de pytest o logs de la herramienta)
```

### 💻 Entorno
- **Sistema Operativo:** Windows / Linux / macOS
- **IDE:** Google Antigravity IDE / VS Code
- **Python / Entorno:** Python 3.11+ / PHP 8.2+
