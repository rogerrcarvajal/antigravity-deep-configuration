# 50 - Directrices de Seguridad, QA, DevOps y Despliegue Cloud-Native

Aplica a la validación de código, pruebas automatizadas, empaquetado en contenedores y pipelines de despliegue a la nube.

---

## 1. Auditoría de Seguridad Zero-Trust y OWASP Top 10
Todo agente o desarrollador debe auditar activamente:
- **Cero Secretos en Código:** Prohibido estrictamente incluir API keys, tokens o credenciales en archivos del repositorio. Usar variables de entorno (`.env` local y GitHub Secrets en CI/CD).
- **Inyección SQL y Comandos:**
  - En PHP: Sentencias preparadas con PDO obligatorias.
  - En Python: Consultas parametrizadas con `asyncpg` o SQLAlchemy, y validación estricta de payloads con Pydantic v2.
- **Autenticación y Sesiones:** Tokens seguros, expiración controlada y cabeceras de protección (`HttpOnly`, `SameSite=Lax`, `Secure`).
- **Sanitización XSS y CSRF:** Escape de salidas HTML y validación de tokens anti-CSRF en peticiones mutantes.

---

## 2. Automatización DevOps con GitHub MCP
- El agente `qa-security-auditor` se encarga de:
  1. Validar que la suite de pruebas unitarias y linters pase al 100% con 0 fallos antes de promover código.
  2. Crear ramas de feature limpias: `feature/nombre-de-la-tarea` o `feature/s<X>-<Y>-<slug>`.
  3. Crear Pull Requests utilizando la herramienta MCP de GitHub con trazabilidad `Ref #X` (sin auto-cierre indebido), resumen de cambios y estado de CI.

---

## 3. Estándares Cloud-Native y Despliegue Multi-Cloud (GCP, AWS)
- **Contenedores OCI (Docker):**
  - Todo microservicio o aplicación cloud-native debe contar con un `Dockerfile` multi-stage que corra bajo un usuario sin privilegios (`appuser`).
  - Puerto dinámico gestionado mediante la variable de entorno `PORT` (por defecto `8080`).
  - Healthcheck `/health` configurado en el contenedor para orquestadores en la nube.
- **Pipelines CI/CD desde GitHub Actions:**
  - Automatizar la construcción y publicación de imágenes en registros de contenedores:
    * **Google Cloud Platform:** Google Artifact Registry / Google Container Registry (GCR) y despliegue a **Cloud Run**.
    * **Amazon Web Services:** Amazon ECR y despliegue a **AWS App Runner** o **AWS ECS Fargate**.
    * **PaaS Modernas:** Despliegue automatizado en Render, Railway o Fly.io.
  - Autenticación en la nube mediante Workload Identity Federation o credenciales seguras inyectadas en GitHub Secrets (`GCP_SA_KEY`, `AWS_ACCESS_KEY_ID`, etc.).
