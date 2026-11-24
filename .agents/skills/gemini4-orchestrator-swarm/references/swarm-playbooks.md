# Playbooks Prácticos de Orchestrator y `/swarm` con Carbon · Neon · Hydrogen

## Playbook 1: Arquitectura Crítica en Sesión Única con `Orchestrator (Carbon)`

Para diseñar e implementar un subsistema complejo sin administrar múltiples agentes manualmente:

1. Selecciona **`Orchestrator (Carbon)`** (o **`Gemini 4 Carbon (Medium/High)`**) en el selector de modelos.
2. Si existe grafo en `graphify-out/`, el orquestador consultará primero `graphify query` / `path` ahorrando hasta un 80% de tokens.
3. **Carbon** formulará el plan arquitectónico y supervisará mientras **Hydrogen** escribe el código, ejecuta la suite de pruebas y valida el resultado en bucle hasta 0 errores.

---

## Playbook 2: Enjambre de Élite con la Tríada Completa (`/swarm-pro`)

Cuando un proyecto grande puede dividirse en varios frentes simultáneos sin colisión de archivos:

1. **Título del Swarm:**
   ```json
   swarm{"action": "title", "title": "Despliegue Paralelo Tríada Gemini 4 (Carbon + Neon + Hydrogen)"}
   ```
2. **Distribución Estratégica de Workers (`swarm{action:"add"}`):**
   - **`core-architect`** (`workspace: "share"`, `model: "gemini-4-carbon-high"`): Posee el núcleo de dominio, seguridad o migraciones críticas (`src/domain/`, `src/security/`). Al terminar publica resumen y menciona a `@lead-verifier`.
   - **`api-services`** (`workspace: "share"`, `model: "gemini-4-neon-high"`): Posee controladores, rutas e integraciones de contexto amplio (`src/api/`, `src/services/`). Prohibido editar `src/domain/` o `src/ui/`. Al terminar menciona a `@lead-verifier`.
   - **`ui-and-tests`** (`workspace: "share"`, `model: "gemini-4-hydrogen-high"`): Posee componentes visuales y pruebas automatizadas (`src/ui/`, `tests/`). Al terminar menciona a `@lead-verifier`.
   - **`lead-verifier`** (`workspace: "inherit"`, `model: "gemini-4-carbon-medium"`): Revisa los diffs de los 3 autores, ejecuta la batería completa de tests y reporta en el tablero (`@api-services corrige X` o `@coordinator todo verificado y listo para merge`).

---

## Playbook 3: Auditoría Independiente EGM + Reparación en Paralelo

Combina **Elephant-Goldfish Model (`egm-auditoria`)** con **Gemini 4 Carbon** y **Neon**:

1. **Fase Elephant:** Redacta la especificación o prototipo con `Orchestrator (Carbon)` o `Orchestrator (Neon)`.
2. **Fase Goldfish:** Lanza los 4 peces sin memoria previa (`cliente`, `desconfiado`, `proteccion-datos`, `tecnico`) para detectar puntos ciegos en `goldfish_review_report.md`.
3. **Fase Resolución en `/swarm`:** Tras aprobar qué puntos corregir, despliega un worker por módulo (`Neon` / `Hydrogen` en `workspace: "share"`) y un verificador (`Carbon` en `workspace: "inherit"`) para aplicar las correcciones simultáneamente.

---

## Playbook 4: Fan-Out Programático con `run_workflow`

Para transformaciones o auditorías repetitivas sobre decenas de archivos:

```python
phase("Mapeo Estructural")
archivos = await agent(
    "Lista los archivos del módulo objetivo que requieren revisión. Solo rutas relativas.",
    schema={"type": "array", "items": {"type": "string"}},
    role="Planificador Carbon/Neon",
    model="pro"
)

phase("Inspección Masiva en Paralelo")
hallazgos = await parallel(archivos, lambda f: agent(
    f"Analiza {f} buscando fallos de seguridad, tipado o rendimiento. Responde en máximo 3 puntos concretos.",
    schema={"type": "string"},
    role=f"Revisor {f}",
    model="flash"
))

for archivo, h in zip(archivos, hallazgos):
    log(f"### {archivo}\n{h}")
```
