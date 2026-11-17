# Guía de Orquestación con Gemini 4 (Argon / Hydrogen) y `/swarm` en Antigravity

## 1. Análisis de Modelos Disponibles en tu Plan Gemini Pro

A partir de tu captura de pantalla y la consulta en vivo al motor `swarm{action:"models"}` de Antigravity, tu suscripción **Gemini AI Pro** cuenta con acceso al **100% de cuota** en los siguientes modelos:

| Modelo en Selector UI | ID del Motor | Ciclo de Reinicio | Disponibilidad en Gemini Pro |
| :--- | :--- | :--- | :--- |
| **Orchestrator (Argon)** | `gemini-pro-orchestrator-g1-pro` | **Semanal** (7 días) | ✅ Activo (100%) |
| **Gemini 4 Argon** (`Low` / `Medium` / `High`) | `gemini-4-argon-*` | **Semanal** (7 días) | ✅ Activo (100%) |
| **Gemini 4 Hydrogen** (`Low` / `Medium` / `High` / `XHigh`) | `gemini-4-hydrogen-*` | **Diario** (24 horas) | ✅ Activo (100%) |
| **Claude Opus 5.5 / Sonnet 5.5** (`Low` / `Medium` / `High`) | `claude-*-5-5-*` | **Diario** (24 horas) | ✅ Activo (100%) |
| **Gemini 3.8 Flash** (`Low` / `Medium` / `High`) | `gemini-3.8-flash-*` | **Diario** (24 horas) | ✅ Activo (100%) |
| **GPT-OSS 120B (Medium)** | `gpt-oss-120b-medium` | **Diario** (24 horas) | ✅ Activo (100%) |
| *Gemini 4 Carbon* | *Exclusivo Ultra / Enterprise* | — | 🔒 No incluido en Pro |

> [!TIP]
> **Hallazgo Clave para tu Plan Gemini Pro:**
> Sí tienes disponibles **Gemini 4 Argon**, **Gemini 4 Hydrogen** (¡incluyendo el nivel `XHigh`!) y **`Orchestrator (Argon)`**. El único modelo bloqueado en tu selector es **Gemini 4 Carbon**.
> Además, **Argon** y **Orchestrator (Argon)** tienen **cuota semanal**, mientras que **Hydrogen (`Low` a `XHigh`)** y **Claude 5.5** se recargan **todos los días (cada 24 horas)**.

---

## 2. Cómo Funciona `Orchestrator (Argon)` vs. `/swarm`

```mermaid
flowchart LR
    subgraph Modo 1: Orchestrator (Argon) - 1 Sola Sesión
        O1["🧠 Gemini 4 Argon<br/>(Planifica y Diseña)"] <-->|"Cambio dinámico<br/>en la misma sesión"| O2["⚡ Gemini 4 Hydrogen<br/>(Codifica y Ejecuta Tests)"]
    end

    subgraph Modo 2: /swarm - Enjambre Paralelo en Tablero Compartido
        S0["🎯 Coordinador<br/>(Tú + Agente Principal)"] --> S1["👷 Worker Backend<br/>(workspace: share)"]
        S0 --> S2["🎨 Worker Frontend<br/>(workspace: share)"]
        S0 --> S3["🛡️ Verifier<br/>(workspace: inherit)"]
        S1 & S2 <-->|"Tablero de Mensajes<br/>(@mentions)"| S3
    end
```

1. **`Orchestrator (Argon)`:**
   - No requiere comandos adicionales: basta con dejar seleccionado **`Orchestrator (Argon)`** en el menú desplegable inferior de Antigravity (como aparece en tu captura).
   - **Argon** toma el control al inicio para razonar la arquitectura, y delega automáticamente en **Hydrogen** la escritura de código y ejecución de pruebas. Si una prueba falla, el control regresa a Argon.
2. **Enjambre Nativo (`/swarm` y `/swarm-pro`):**
   - Crea múltiples agentes independientes trabajando **al mismo tiempo** en copias aisladas de tu repositorio (`workspace: "share"`), coordinados a través de un tablero de mensajes en vivo (`open_board`).

---

## 3. Estrategia Inteligente de Cuotas para Usar `/swarm` en Gemini Pro

Dado que en `/swarm` cada worker hereda por defecto el modelo activo de tu conversación:

- **Para tareas individuales o diseño arquitectónico:** Usa **`Orchestrator (Argon)`** o **`Gemini 4 Argon (Medium/High)`**.
- **Antes de lanzar un `/swarm` con varios workers:** Cambia el selector a **`Gemini 4 Hydrogen (High)`** o **`Gemini 4 Hydrogen (XHigh)`** (o pide al coordinador fijar `model: "gemini-4-hydrogen-high"` en los workers). Así todo el enjambre paralelo correrá sobre tu **cuota diaria renovable cada 24h**, dejando intacta tu cuota semanal de Argon.
- **Cambio de modelo en caliente (sin perder contexto):** Si cualquier worker agota su cuota a mitad de una tarea, Antigravity permite cambiar su modelo al instante con `swarm{action:"model", name:"worker", model:"gemini-4-hydrogen-high"}` sin usar `kill`.

---

## 4. Cómo Invocar la Nueva Skill y Workflow

- **Workflow directo:** Escribe `/swarm-pro` o `/swarm` seguido de tu objetivo (ej. *"Refactoriza en paralelo los módulos de autenticación, pagos y notificaciones con un verificador de tests"*).
- **Skill instalada:** [`gemini4-orchestrator-swarm`](../.agents/skills/gemini4-orchestrator-swarm/SKILL.md) (disponible tanto en `.agents/skills/`, `.gemini/skills/` como en `~/.gemini/config/skills/`).
- **Regla activa:** [`gemini4-orchestrator-swarm.md`](../.agents/rules/gemini4-orchestrator-swarm.md) (y global `80-gemini4-orchestrator-and-swarm.md`).
