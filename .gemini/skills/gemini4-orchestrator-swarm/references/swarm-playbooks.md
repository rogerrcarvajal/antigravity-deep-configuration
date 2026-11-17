# Playbooks Prácticos de `/swarm` y `run_workflow` en Antigravity

## Playbook 1: Desarrollo Full-Stack en Paralelo (`/swarm`)

Cuando necesitas construir o refactorizar Backend, Frontend y Pruebas al mismo tiempo sin colisiones:

1. **Título del Swarm:**
   ```json
   swarm{"action": "title", "title": "Feature Full-Stack en Paralelo"}
   ```
2. **Despliegue de Workers (sin colisión de archivos):**
   - **`backend`** (`workspace: "share"`): Posee `src/api/` y `src/models/`. Prohibido tocar `src/ui/`. Al terminar publica el contrato y menciona a `@verifier`.
   - **`frontend`** (`workspace: "share"`): Posee `src/ui/` y `src/components/`. Prohibido tocar `src/api/`. Al terminar menciona a `@verifier`.
   - **`verifier`** (`workspace: "inherit"`): Revisa los diffs de `@backend` y `@frontend`, ejecuta la suite de tests y reporta fallos mencionando al autor correspondiente o a `@coordinator` si todo pasa.

---

## Playbook 2: Auditoría y Corrección Masiva con Verificador Cruzado

1. Lanza N workers por módulo (`tasks` o `add` individual con `workspace: "share"`).
2. Añade 1 `verifier` por cada 3 workers.
3. Usa mensajes cortos referenciando el número de secuencia del tablero (`@verifier revisa #3 y #5`).
4. Antes de cerrar el swarm, pide a cada autor o al coordinador fusionar las ramas de `workspace: "share"` en el workspace principal antes de ejecutar `swarm{action:"kill"}`.

---

## Playbook 3: Fan-Out Programático con `run_workflow`

Cuando tienes una lista de archivos o módulos que deben analizarse o transformarse siguiendo exactamente la misma plantilla sin necesidad de que los agentes conversen entre sí en un tablero:

```python
phase("Descubrimiento")
archivos = await agent(
    "Lista los archivos principales del módulo a revisar. Solo rutas relativas.",
    schema={"type": "array", "items": {"type": "string"}},
    role="Explorador"
)

phase("Análisis en Paralelo")
reportes = await parallel(archivos, lambda f: agent(
    f"Analiza {f} buscando problemas de tipado, seguridad o acoplamiento. Resume en máximo 3 puntos.",
    schema={"type": "string"},
    role=f"Auditor {f}",
    model="flash"
))

for archivo, reporte in zip(archivos, reportes):
    log(f"### {archivo}\n{reporte}")
```
