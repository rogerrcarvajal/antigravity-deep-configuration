# Playbooks Prácticos de `/swarm` y `run_workflow` con Gemini 4 Neon

## Playbook 1: Enjambre Full-Stack de Alto Rendimiento con Gemini 4 Neon (`/swarm-pro`)

Aprovecha la ventana de **1M de tokens** y la **cuota diaria** de **Gemini 4 Neon** junto con **Hydrogen**:

1. **Preparación:** Selecciona **`Gemini 4 Neon (Medium o High)`** u **`Orchestrator (Neon)`** en tu selector de modelo.
2. **Título del Swarm:**
   ```json
   swarm{"action": "title", "title": "Feature Full-Stack con Gemini 4 Neon"}
   ```
3. **Despliegue de Workers (sin colisión de archivos):**
   - **`architect-backend`** (`workspace: "share"`, `model: "gemini-4-neon-high"`): Posee `src/api/` y `src/domain/`. Diseña e implementa endpoints y lógica compleja. Prohibido tocar `src/ui/`. Al terminar publica resumen y menciona a `@verifier`.
   - **`frontend-ui`** (`workspace: "share"`, `model: "gemini-4-hydrogen-high"`): Posee `src/ui/` y `src/components/`. Construye componentes reactivos/glassmorphic. Prohibido tocar `src/api/`. Al terminar menciona a `@verifier`.
   - **`verifier`** (`workspace: "inherit"`, `model: "gemini-4-neon-high"`): Revisa los diffs de `@architect-backend` y `@frontend-ui`, ejecuta la suite de pruebas y reporta en el tablero (`@architect-backend corrige X` o `@coordinator listo para merge`).

---

## Playbook 2: Auditoría de Contexto Masivo (1M Tokens) + Corrección en Paralelo

Cuando necesitas analizar un repositorio grande o documento técnico extenso aprovechando el millón de tokens de **Gemini 4 Neon**:

1. **Consulta previa con Graphify:** Obtén el mapa estructural con `graphify query` o `graphify path`.
2. **Despliegue en `/swarm`:**
   - Asigna a un worker `neon-analyzer` (`gemini-4-neon-xhigh`, `workspace: "inherit"`) la inspección profunda de contratos y dependencias críticas.
   - Asigna workers ejecutores (`gemini-4-neon-medium` o `gemini-4-hydrogen-high`, `workspace: "share"`) por cada módulo a corregir.
   - Añade 1 `verifier` por cada 3 autores.
3. **Cierre seguro:** Fusiona las ramas de `workspace: "share"` en tu copia principal antes de ejecutar `swarm{action:"kill"}`.

---

## Playbook 3: Fan-Out Programático con `run_workflow`

Para procesar lotes de archivos en paralelo mediante script Python sin sobrecargar el tablero de `/swarm`:

```python
phase("Descubrimiento con Contexto Amplio")
archivos = await agent(
    "Lista los archivos clave del proyecto que requieren actualización o auditoría. Solo rutas relativas.",
    schema={"type": "array", "items": {"type": "string"}},
    role="Explorador Neon",
    model="pro"
)

phase("Ejecución Paralela Optimizada en Coste")
reportes = await parallel(archivos, lambda f: agent(
    f"Revisa {f} buscando vulnerabilidades, errores de tipado o deuda técnica. Máximo 3 puntos accionables.",
    schema={"type": "string"},
    role=f"Auditor {f}",
    model="flash"
))

for archivo, reporte in zip(archivos, reportes):
    log(f"### {archivo}\n{reporte}")
```
