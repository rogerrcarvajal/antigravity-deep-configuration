# Matriz de Modelos Gemini 4 (Carbon · Neon · Hydrogen) y Gestión de Cuotas en Gemini Pro

## 1. Catálogo Activo Verificado en tu Cuenta (`swarm{action:"models", all:true}`)

| Nivel | Modelos Activos | Estado Actual | Perfil y Ventaja Competitiva | Cuándo Elegirlo |
| :--- | :--- | :--- | :--- | :--- |
| **Orquestadores Nativos** | `Orchestrator (Carbon)` (`gemini-pro-orchestrator`)<br>`Orchestrator (Neon)` (`gemini-pro-orchestrator-neon`) | ✅ **Activos** (Recarga 24h) | Alternancia automática entre cerebro planificador (**Carbon** o **Neon**) y ejecutor veloz (**Hydrogen**) en la misma sesión. | Usa **Orchestrator (Carbon)** para retos de alta complejidad arquitectónica y **Orchestrator (Neon)** para desarrollo rápido o contextos de 1M tokens. |
| **Frontera Profunda** | `Gemini 4 Carbon` (`Low`, `Medium`, `High`) | ✅ **Activo** (Recarga 24h) | Máxima capacidad de razonamiento multi-paso, abstracción arquitectónica y depuración profunda. | Diseño de sistemas (*Elephant* en EGM), refactorizaciones delicadas, seguridad y verificación crítica. |
| **Frontera Ágil (1M)** | `Gemini 4 Neon` (`Low`, `Medium`, `High`, `XHigh`) | ✅ **Activo** (Recarga 24h) | **Ventana unificada de 1M tokens (In/Out)**, 3x más rápido que Carbon y excelente coste/tarea. | Programación intensiva, lectura de repositorios completos y workers principales en `/swarm`. |
| **Alta Velocidad** | `Gemini 4 Hydrogen` (`Low`, `Medium`, `High`, `XHigh`) | ✅ **Activo** (Recarga 24h) | Ejecución ultrarrápida y alto rendimiento espacial (especialmente en `High` y `XHigh`). | Workers ejecutores en `/swarm`, tests, maquetación UI y sustituto directo de Flash 3.8. |
| **Contraste Externo** | `Claude Opus 5.5` / `Sonnet 5.5` (`Low`, `Medium`, `High`) | ✅ **Activos** (Recarga 24h) | Segunda perspectiva de otra familia de modelos frontera. | Auditorías *Goldfish* (`egm-auditoria`) y rol `verifier` en `/swarm`. |
| **En Retirada** | `Gemini 4 Argon` / `Orchestrator (Argon)`<br>`Gemini 3.8 Flash` | ⚠️ **Leaving Soon** | Modelos de transición previos a la activación completa de Carbon + Neon + Hydrogen. | No iniciar nuevos workflows fijos sobre ellos: migra `Argon` → **`Carbon`/`Neon`** y `3.8 Flash` → **`Hydrogen`**. |

---

## 2. Cómo Funciona el Modo Orchestrator con Carbon vs. Neon

1. **`Orchestrator (Carbon)` (`gemini-pro-orchestrator`):**
   - Implementa el flujo clásico de máxima precisión de Antigravity: **Gemini 4 Carbon** descompone el problema, diseña contratos e invariantes, y delega la codificación línea por línea y ejecución de comandos en **Gemini 4 Hydrogen**. Si una prueba falla, **Carbon** reexamina la causa raíz antes de que Hydrogen vuelva a editar.
2. **`Orchestrator (Neon)` (`gemini-pro-orchestrator-neon`):**
   - Mantiene la misma mecánica dual pero usando **Gemini 4 Neon** (3 veces más veloz y con ventana unificada de **1 millón de tokens**) como planificador, ideal cuando la tarea requiere absorber decenas de archivos largos con respuesta casi instantánea.

---

## 3. Cadena de Respaldo de Cuotas (Failover sin Pérdida de Contexto)

Si durante un `/swarm` intensivo un modelo consume su presupuesto del ciclo actual, aplica cambio en caliente (`swarm{action:"model", name, model}`):

1. **`gemini-4-carbon-high` / `medium`** (Razonamiento máximo)
   ↓ *failover en caliente a*
2. **`gemini-4-neon-xhigh` / `high`** (1M tokens, razonamiento frontera rápido)
   ↓ *failover en caliente a*
3. **`gemini-4-hydrogen-xhigh` / `high`** (Ejecución veloz de alta capacidad)
   ↓ *o contraste en*
4. **`claude-sonnet-5-5-high` / `claude-opus-5-5-medium`**.
