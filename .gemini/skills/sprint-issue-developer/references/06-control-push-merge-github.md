# 06 - Control de Push, Pull Requests y Merge en GitHub

Este documento fija los límites inviolables de los agentes frente al control de versiones remoto, en cualquier proyecto.

---

## 1. Prohibiciones Absolutas de los Agentes
- Los agentes **NUNCA** ejecutan `git push` hacia `main` ni hacen merge de Pull Requests, ni por el servidor MCP de GitHub ni por línea de comandos.
- Los agentes **NUNCA** abren un Pull Request directamente: preparan la rama, el código y la descripción; el desarrollador ejecuta el push y crea el PR.

## 2. Estándar de Entrega por Issue
- Toda actividad se desarrolla en una rama `feature/...` o `fix/...` asociada a un issue.
- La descripción del PR debe incluir: referencia al issue con `Ref #N` (NUNCA `Closes #N` ni `Fixes #N`: el cierre del issue lo hace manualmente la persona reseñadora), cómo cumple cada criterio de aceptación y evidencia de que no rompe nada (salida de la suite de pruebas del repo).
- En `wellness-platform-team2` la evidencia mínima es: `python tests/run_tests_standalone.py` (6 tests) y `pytest tests/test_main.py` (11 tests) en verde.

## 3. Aprobación y Merge
- El merge a `main` lo realiza **ÚNICAMENTE** la persona reseñadora designada del proyecto (en la maestría: la profesora). Nadie más mergea, ni siquiera el autor del PR.
