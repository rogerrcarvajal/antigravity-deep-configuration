---
trigger: model_decision
description: Orquesta la triada completa Gemini 4 (Carbon, Neon, Hydrogen) y los modos Orchestrator (Carbon/Neon) junto con /swarm y run_workflow en el plan Gemini Pro.
---

# Gobernanza de la Tríada Gemini 4 (Carbon · Neon · Hydrogen) y `/swarm`

1. **Roles de la Tríada Gemini 4 Activa en Gemini Pro:**
   - **`Orchestrator (Carbon)`** (`gemini-pro-orchestrator`) y **`Gemini 4 Carbon`** (`Low`, `Medium`, `High`): Razonamiento profundo de largo horizonte. Úsalos para diseño arquitectónico complejo, decisiones críticas (*Elephant*), seguridad y verificación estricta (en modo Orchestrator, **Carbon** planifica y **Hydrogen** ejecuta en la misma sesión).
   - **`Orchestrator (Neon)`** (`gemini-pro-orchestrator-neon`) y **`Gemini 4 Neon`** (`Low`, `Medium`, `High`, `XHigh`): Ventana unificada de **1 millón de tokens (In/Out)** y velocidad **3x superior a Carbon**. Úsalos para programación ágil diaria, lectura de repositorios completos y workers de lógica compleja en `/swarm`.
   - **`Gemini 4 Hydrogen`** (`Low`, `Medium`, `High`, `XHigh`): Ejecutor de alta velocidad. Úsalo para workers rápidos en `/swarm`, UI, pruebas y tareas ligeras.
   - **Transición de Modelos (`Leaving Soon`):** No fijes nuevos flujos sobre `Gemini 4 Argon` ni `Gemini 3.8 Flash`; utiliza **`Carbon` / `Neon`** en lugar de Argon y **`Hydrogen`** en lugar de 3.8 Flash.
2. **Protocolo de Enjambre (`/swarm` y `/swarm-pro`):**
   - Verifica modelos y cuotas con `swarm{action:"models"}`.
   - Divide el trabajo sin colisión de archivos (1 archivo/módulo = 1 worker autor con `workspace: "share"`).
   - Incluye siempre **1 verificador** (`workspace: "inherit"`, en `Carbon`, `Neon` o `Claude 5.5`) por cada 2 a 4 autores.
   - Si un modelo alcanza límite de cuota, haz relevo en caliente con `swarm{action:"model", name, model}` (`Carbon` → `Neon XHigh` → `Hydrogen XHigh`) sin usar `kill`.
   - Integra siempre los cambios de `workspace: "share"` o `"branch"` antes de ejecutar `kill` sobre un worker autor.
3. **Orquestación Programática (`run_workflow`):**
   - Para procesamiento repetitivo por lotes sobre listas de archivos sin debate en tablero compartido, prefiere `run_workflow` con `parallel()` o `pipeline()`.
