# Guía Maestra: Tríada Gemini 4 (Carbon · Neon · Hydrogen), Orchestrator y `/swarm` en Antigravity

## 1. Catálogo Completo Verificado en tu Plan Gemini Pro

Tras la habilitación oficial de **Gemini 4 Carbon** en el plan **Gemini AI Pro** (verificado en vivo vía `swarm{action:"models", all:true}` y tu selector de modelos), cuentas ahora con el **ecosistema Gemini 4 al 100%**:

| Modelo en Selector UI | ID Interno (`model`) | Estado y Cuota | Perfil Técnico | Uso Recomendado |
| :--- | :--- | :--- | :--- | :--- |
| **Orchestrator (Carbon)** 🏆 | `gemini-pro-orchestrator` | ✅ Activo (Recarga 24h) | **Carbon (Planner) ↔ Hydrogen (Executor)** | Diseño arquitectónico complejo + codificación y tests automáticos en una sola sesión. |
| **Gemini 4 Carbon** (`Low` / `Medium` / `High`) 🧠 | `gemini-4-carbon-*` | ✅ Activo (Recarga 24h) | Razonamiento frontera de largo horizonte | Arquitectura pura (*Elephant*), seguridad, algoritmos difíciles y `verifier` líder en `/swarm`. |
| **Orchestrator (Neon)** ⭐ | `gemini-pro-orchestrator-neon` | ✅ Activo (Recarga 24h) | **Neon (1M Tokens) ↔ Hydrogen (Executor)** | Desarrollo ágil diario con contexto masivo de 1 millón de tokens y alta velocidad. |
| **Gemini 4 Neon** (`Low` / `Medium` / `High` / `XHigh`) ⚡ | `gemini-4-neon-*` | ✅ Activo (Recarga 24h) | **1M tokens unificados (In/Out)** · 3x más rápido que Carbon | Lectura de repositorios completos, refactorización multi-archivo y workers pesados de `/swarm`. |
| **Gemini 4 Hydrogen** (`Low` / `Medium` / `High` / `XHigh`) 🚀 | `gemini-4-hydrogen-*` | ✅ Activo (Recarga 24h) | Alta velocidad y eficiencia espacial | Workers paralelos rápidos en `/swarm`, UI, tests y sustituto directo de Flash 3.8. |
| **Claude Opus 5.5 / Sonnet 5.5** (`Low` / `Medium` / `High`) | `claude-*-5-5-*` | ✅ Activo (Recarga 24h) | Contraste multi-familia | Revisores independientes (*Goldfish* / `verifier`). |
| **GPT-OSS 120B (Medium)** | `gpt-oss-120b-medium` | ✅ Activo (Recarga 24h) | Alternativa Open-Weight | Pruebas comparativas. |
| *Gemini 4 Argon / Orchestrator (Argon)* | `gemini-4-argon-*` | ⚠️ **Leaving Soon** | En retirada programada | Migrar flujos a **Gemini 4 Carbon** y **Gemini 4 Neon**. |
| *Gemini 3.8 Flash* | `gemini-3.8-flash-*` | ⚠️ **Leaving Soon** | En retirada programada | Migrar flujos ligeros a **Gemini 4 Hydrogen (`Low`/`Medium`)**. |

---

## 2. Arquitectura de Coordinación: `Orchestrator` vs. `/swarm-pro`

```mermaid
flowchart LR
    subgraph Modo A: Orchestrator Nativo (1 Sola Sesión)
        P1["🧠 Carbon (Arquitectura Crítica)<br/>o ⚡ Neon (1M Tokens Ágil)"] <-->|"Relevo automático<br/>en vivo"| E1["🚀 Hydrogen<br/>(Escribe Código + Corre Tests)"]
    end

    subgraph Modo B: /swarm-pro (Enjambre Paralelo con la Tríada Gemini 4)
        C0["🎯 Coordinador<br/>(Carbon / Neon)"] --> W1["🧠 Core / Dominio<br/>Carbon (High) · share"]
        C0 --> W2["⚡ APIs / Servicios (1M)<br/>Neon (High) · share"]
        C0 --> W3["🚀 UI / Tests Rápidos<br/>Hydrogen (High) · share"]
        C0 --> V1["🛡️ Lead Verifier<br/>Carbon (Medium) / Claude 5.5 · inherit"]
        W1 & W2 & W3 <-->|"Tablero (@mentions)"| V1
    end
```

### Cómo aprovechar el Modo `Orchestrator` ahora con Carbon y Neon:
1. **`Orchestrator (Carbon)` (`gemini-pro-orchestrator`):** Es la combinación estrella mostrada en los benchmarks oficiales de Antigravity. **Carbon** piensa la arquitectura, resuelve dependencias complejas y supervisa, mientras **Hydrogen** ejecuta las ediciones y corre las pruebas rápidamente. Si algo falla, **Carbon** retoma el volante al instante.
2. **`Orchestrator (Neon)` (`gemini-pro-orchestrator-neon`):** Usa la misma arquitectura dual, pero con **Neon** (1M de tokens unificados y 3x más rápido que Carbon) como planificador, ideal cuando necesitas iterar a gran velocidad sobre bases de código extensas.

---

## 3. Reglas de Oro Operativas

1. **Adiós a los modelos *Leaving Soon*:** Sustituye `Gemini 4 Argon` por **`Gemini 4 Carbon`** (cuando busques máxima profundidad) o **`Gemini 4 Neon`** (cuando busques velocidad y 1M de contexto), y sustituye `Gemini 3.8 Flash` por **`Gemini 4 Hydrogen`**.
2. **Ahorro de contexto + Tríada Gemini 4:** Combina el grafo de conocimiento **`graphify`** (80% menos tokens en consultas de arquitectura) con **`Orchestrator (Carbon)`** / **`Orchestrator (Neon)`** y auditorías **`egm-auditoria`** antes de pasar a producción.
3. **Failover continuo en `/swarm`:** Si en una sesión masiva se agota la cuota de un modelo, cambia cualquier worker en caliente con `swarm{action:"model", name, model}` siguiendo la cascada `Carbon` → `Neon (XHigh)` → `Hydrogen (XHigh)` sin perder el historial de trabajo.
