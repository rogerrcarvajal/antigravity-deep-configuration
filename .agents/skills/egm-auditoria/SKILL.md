---
name: egm-auditoria
description: Implementa la estrategia de auditoria del Google Elephant-Goldfish Model (EGM) en Antigravity usando subagentes independientes sin memoria (Goldfish) para revisar especificaciones, codigo y apps antes de produccion o entrega a clientes.
---

# EGM Auditoría · Estrategia Elephant-Goldfish Model (Google)

Implementación nativa en Google Antigravity del **Elephant-Goldfish Model (EGM)** de Google combinado con el **Kit EGM de Auditoría en Español**.

> **Principio Rector:** *«Diseña con un Elefante. Revisa con un Pez Dorado.»*
> - **Elephant (Elefante):** Sesión principal con memoria completa del proyecto, contexto de negocio, arquitectura y decisiones previas. Comprende, planifica (`concepts_brief.md` / `design_draft.md`) y ejecuta cambios.
> - **Goldfish (Peces Dorados):** Subagentes aislados **sin memoria** (`invoke_subagent`), de solo lectura y contexto cero. No conocen la conversación previa donde se creó la idea o el código; juzgan únicamente lo que está escrito frente al contexto real del negocio y estándares técnicos, exponiendo supuestos ocultos, fallos lógicos y brechas antes de entregar al cliente.

---

## Cuándo activar esta Skill

- Antes de iniciar la codificación de un módulo complejo o feature crítico (auditoría de especificación / PRD / plan).
- Antes de entregar una web, app o sistema a un cliente o pasar a producción.
- Cuando el usuario solicite: *"auditar con EGM"*, *"revisar con peces"*, *"auditoría Elephant-Goldfish"*, *"revisión independiente sin sesgo"*, o `/egm-auditar`.

---

## Flujo de Trabajo en 2 Modos

### Modo A: Auditoría de Diseño y Especificación (Pre-Codificación)
Ideal antes de escribir código, usando las skills oficiales del plugin EGM (`~/.gemini/config/plugins/egm/`):
1. **Elephant - Comprensión y Planificación:**
   - Explorar el problema (`egm-brainstorm`) y generar el borrador de especificación (`egm-draft`) o documento de diseño.
2. **Goldfish - Revisión Independiente (5 perspectivas):**
   - Lanzar subagentes de contexto limpio (`invoke_subagent` con `TypeName: "research"` o `"self"` sin pasar el historial de chat) usando los revisores oficiales de EGM (`agents/comprehension.md`, `agents/design_critic.md`, `agents/structural.md`, `agents/implementation_readiness.md`, `agents/style.md`).
3. **Resolución Humana (`egm-resolve`):**
   - Presentar hallazgos priorizados al usuario para que tome las decisiones arquitectónicas antes de programar.

### Modo B: Auditoría de App / Web / Código (Kit EGM en Español - 4 Peces)
Ideal para auditar aplicaciones web, landing pages, formularios, código fuente o documentos antes de mostrarlos a un cliente:

1. **Verificar o preparar los archivos de auditoría:**
   - **Objetivo (`TargetFile`):** Archivo o módulo a auditar (ej. `index.html`, `app.py`, `docs/design.md`).
   - **Contexto real (`contexto/`):** `notas-del-negocio.md` y `resenas.md` (plantillas disponibles en `plantilla-contexto/` dentro de esta skill).
   - **Los 4 Peces (`peces/`):**
     1. `peces/cliente.md` — Cliente nuevo desde móvil, sin conocer el negocio.
     2. `peces/desconfiado.md` — Usuario escéptico buscando trampas, letra pequeña o contradicciones.
     3. `peces/proteccion-datos.md` — Auditor de privacidad, RGPD/GDPR, formularios, cookies y exposición de datos.
     4. `peces/tecnico.md` — Técnico que verifica si lo que promete la pantalla ocurre realmente en el código (pagos, concurrencia, validaciones, secretos expuestos).
   - **Estándar (`Standards`):** `peces/estandar-web-negocio.md`.

2. **Confirmar configuración con el usuario** (archivo objetivo, peces activos, archivos de contexto) salvo que ya venga explícito.

3. **Lanzar los 4 Peces en paralelo con contexto aislado:**
   - Invocar 4 llamadas simultáneas a `invoke_subagent` (`TypeName: "research"`, `Model: "inherit"`).
   - **Regla estricta de aislamiento Goldfish:** En el `Prompt` del subagente **NO** incluir explicaciones previas de por qué el código se hizo así ni historial de la conversación. Entregarle únicamente:
     - Su rol exacto (contenido de su archivo `peces/<rol>.md`).
     - El estándar (`peces/estandar-web-negocio.md`).
     - Las rutas exactas del `TargetFile` y del `GoldfishContext` (`contexto/`).
     - La instrucción de solo lectura y formato de salida en español.

4. **Síntesis y Deduplicación (`goldfish_review_report.md`):**
   - Consolidar los 4 informes en un reporte unificado en español.
   - Eliminar duplicados y verificar cada hallazgo contra el código real.
   - Clasificar por gravedad:
     - 🔴 **Bloqueante:** Fallos críticos de seguridad, funcionalidad rota, promesas falsas o datos expuestos.
     - 🟡 **Importante:** Fricción severa de UX, ambigüedades de negocio o validaciones faltantes.
     - 🟢 **Detalle:** Mejoras menores de claridad, accesibilidad o pulido.

5. **Decisión del Usuario (Human-in-the-Loop):**
   - Presentar el resumen y preguntar al usuario qué hallazgos desea corregir antes de modificar una sola línea de código.
   - Si se aplican correcciones, ofrecer una nueva ronda Goldfish (máximo 5 rondas) sobre el archivo actualizado.
