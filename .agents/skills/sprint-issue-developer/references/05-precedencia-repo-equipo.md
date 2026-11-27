# 05 - Precedencia de Reglas del Repositorio y Preservación del Stack

Este documento define la jerarquía entre las reglas globales del entorno y las convenciones propias de cada repositorio, especialmente en proyectos colaborativos o académicos.

---

## 1. Precedencia del AGENTS.md del Repositorio
- Si el workspace contiene un `AGENTS.md`, `llms.txt` o carpeta `.agents/` propia (ej. `wellness-platform-team2`), sus convenciones **PREVALECEN** sobre las reglas globales `00-50` en todo lo que ambas regulen.
- Las reglas globales solo aplican en lo que el repositorio no defina: complementan, nunca sustituyen.

## 2. Preservación del Stack Existente
- **Prohibido** migrar gestores de paquetes, frameworks, estructura de directorios, estilos de código o pipelines de un proyecto colaborativo sin un issue aprobado que lo ordene.
- En particular, para `wellness-platform-team2`: se respetan `requirements.txt`, el `Dockerfile` existente, la estructura `src/`, `assets/`, `docs/` y el workflow `ci_cd_cloud_run.yml` tal como están en `main`.
- Las mejoras de stack se proponen como issue/PR, nunca como cambio directo.

## 3. Trabajo en Equipo
- Las decisiones de arquitectura acordadas con los compañeros de equipo (documentadas en `docs/` o ADRs) forman parte de las convenciones del repositorio y tienen la misma precedencia.
