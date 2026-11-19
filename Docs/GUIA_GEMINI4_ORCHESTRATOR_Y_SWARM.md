# Guía de Orquestación con Gemini 4 (Neon / Argon / Hydrogen) y `/swarm` en Antigravity

## 1. Análisis de Modelos Disponibles en tu Plan Gemini Pro (Actualización Gemini 4 Neon)

A partir de tu nueva captura de pantalla y la verificación en vivo con `swarm{action:"models", all:true}`, tu suscripción **Gemini AI Pro** incorpora ahora **`Gemini 4 Neon`** y **`Orchestrator (Neon)`** al 100% de cuota:

| Modelo en Selector UI | ID del Motor | Ciclo de Reinicio | Ventana y Perfil | Estado en Gemini Pro |
| :--- | :--- | :--- | :--- | :--- |
| **Orchestrator (Neon)** ⭐ | `gemini-pro-orchestrator-neon` | **Diario (24 horas)** | **1M tokens unificados** · Neon + Hydrogen | ✅ Activo (100%) |
| **Gemini 4 Neon** (`Low` / `Medium` / `High` / `XHigh`) ⭐ | `gemini-4-neon-*` | **Diario (24 horas)** | **1M tokens (In/Out)** · 3x más rápido que Carbon | ✅ Activo (100%) |
| **Gemini 4 Hydrogen** (`Low` / `Medium` / `High` / `XHigh`) | `gemini-4-hydrogen-*` | **Diario (24 horas)** | Alta velocidad y eficiencia | ✅ Activo (100%) |
| **Orchestrator (Argon)** | `gemini-pro-orchestrator-g1-pro` | **Semanal (7 días)** | Coordinación Argon + Hydrogen | ✅ Activo (100%) |
| **Gemini 4 Argon** (`Low` / `Medium` / `High`) | `gemini-4-argon-*` | **Semanal (7 días)** | Razonamiento profundo (Reserva) | ✅ Activo (100%) |
| **Claude Opus 5.5 / Sonnet 5.5** (`Low` / `Medium` / `High`) | `claude-*-5-5-*` | **Diario (24 horas)** | Contraste y verificación cruzada | ✅ Activo (100%) |
| **Gemini 3.8 Flash** (`Low` / `Medium` / `High`) | `gemini-3.8-flash-*` | **Diario (24 horas)** | Tareas ligeras y subagentes masivos | ✅ Activo (100%) |
| **GPT-OSS 120B (Medium)** | `gpt-oss-120b-medium` | **Diario (24 horas)** | Alternativa Open-Weight | ✅ Activo (100%) |
| *Gemini 4 Carbon* | *Exclusivo Ultra / Enterprise* | — | — | 🔒 No incluido en Pro |

> [!IMPORTANT]
> **Por qué Gemini 4 Neon es tu nuevo modelo estrella en Gemini Pro:**
> 1. **1 Millón de Tokens Unificados (Entrada y Salida):** Permite analizar repositorios completos, documentos técnicos extensos y emitir grandes bloques de código sin recortes.
> 2. **Rendimiento de Programación Frontera a 3x la Velocidad de Carbon:** Diseñado específicamente para programación compleja y flujos agénticos (*tool use*, terminal, refactorización multi-archivo) optimizando el coste por tarea.
> 3. **Cuota Diaria (24h) en lugar de Semanal:** A diferencia de `Argon` y `Orchestrator (Argon)` (cuya cuota tarda **7 días** en reiniciarse), **`Gemini 4 Neon`** (`Low` a `XHigh`) y **`Orchestrator (Neon)`** se recargan **todos los días cada 24 horas**.

---

## 2. Cómo Funcionan `Orchestrator (Neon)` vs. `Orchestrator (Argon)` vs. `/swarm`

```mermaid
flowchart LR
    subgraph Modo 1: Orchestrator (Neon) - Uso Diario Recomendado (Cuota 24h)
        N1["⚡🧠 Gemini 4 Neon (1M Tokens)<br/>(Planifica, Razonamiento Código)"] <-->|"Handoff dinámico<br/>en la misma sesión"| N2["🚀 Gemini 4 Hydrogen<br/>(Edición Rápida y Tests)"]
    end

    subgraph Modo 2: /swarm-pro - Enjambre Paralelo en Tablero Compartido
        S0["🎯 Coordinador: Neon (High)"] --> S1["👷 Worker Core/Backend<br/>Neon (High) · workspace: share"]
        S0 --> S2["🎨 Worker UI/Tests<br/>Hydrogen (High) · workspace: share"]
        S0 --> S3["🛡️ Verifier<br/>Neon (High) / Claude 5.5 · workspace: inherit"]
        S1 & S2 <-->|"Tablero de Mensajes (@mentions)"| S3
    end
```

1. **`Orchestrator (Neon)` (Tu nuevo modo predeterminado):**
   - Selecciónalo directamente en el selector inferior de Antigravity.
   - Utiliza **Gemini 4 Neon** (con su ventana de 1M de tokens y alta capacidad de programación) como cerebro planificador y delega la ejecución mecánica en **Hydrogen**, renovando tu cuota cada 24 horas.
2. **`Orchestrator (Argon)` (Tu reserva estratégica semanal):**
   - Guárdalo para cuando quieras una segunda opinión arquitectónica de Argon o como respaldo si en un día de trabajo extremo llegas al límite diario de Neon.
3. **Enjambre Nativo (`/swarm` y `/swarm-pro`):**
   - Despliega múltiples agentes trabajando en paralelo sobre copias aisladas (`workspace: "share"`) combinando **Neon** (para módulos complejos de backend/arquitectura) y **Hydrogen** (para subtareas rápidas y UI), todos bajo **cuota diaria**.

---

## 3. Cómo Sacarle el Máximo Provecho Ahora Mismo

- **Para el 90% de tu desarrollo diario y tareas complejas:** Selecciona **`Orchestrator (Neon)`** o **`Gemini 4 Neon (Medium / High)`**.
- **Para contextos gigantes o refactorizaciones de repositorio completo:** Selecciona **`Gemini 4 Neon (High o XHigh)`** (1M de tokens unificados + apoyo del grafo `graphify`).
- **Para lanzar un enjambre paralelo (`/swarm` o `/swarm-pro`):** Inicia con **`Gemini 4 Neon (Medium o High)`** activo para que tanto el coordinador como los workers operen sobre cuota diaria renovable cada 24h.
