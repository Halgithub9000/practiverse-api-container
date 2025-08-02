# Practiverse API Container

Este proyecto implementa una API backend en Python usando FastAPI para la generación automática de perfiles profesionales de estudiantes universitarios a partir de documentos (CVs en PDF) almacenados en Google Cloud Storage y procesados con modelos de lenguaje (Anthropic Claude).

## Estructura del Proyecto

- `backend/`: Código fuente del backend (FastAPI).
  - `apis/`: Endpoints de la API (`document_operations.py`, `student_profile.py`).
  - `services/`: Lógica de negocio (servicios para GCS y generación de perfiles).
  - `constants/`: Plantillas y constantes (ej. prompt para el modelo LLM).
  - `.env`: Variables de entorno para el backend.
  - `Makefile`: Automatización de tareas comunes.
- `requirements/`: Dependencias Python.
- `.devcontainer/`: Configuración para desarrollo en contenedores (VS Code).
- `.github/`: Workflows de CI/CD y dependabot.

## Características

- **Carga y extracción de texto de PDFs** almacenados en Google Cloud Storage.
- **Generación de perfiles estudiantiles** en formato JSON usando un modelo LLM (Anthropic Claude).
- **Endpoints REST** para subir, listar y procesar documentos.
- **Rate limiting** y CORS configurados.
- **Automatización** con Makefile para tareas de desarrollo y calidad de código.
- **Configuración lista para Dev Containers** en VS Code.

## Instalación y Uso

1. **Requisitos**:

   - Docker o Podman
   - Visual Studio Code (recomendado con Dev Containers)
   - Acceso a clave de servicio Google Cloud Storage

2. **Variables de entorno**:

   - Configura los archivos `.env` en `backend/`.
   - Configura secretos, creando carpeta poc-files en `backend/` con archivo practiverse-gscredentials.json.
   - solicitar .env y secretos a [camilo.severino.gonzalez@gmail.com](mailto:camilo.severino.gonzalez@gmail.com)

3. **Arranque en Dev Container**:

   - Abre el proyecto en VS Code y selecciona "Reopen in Container".
   - Se instalarán automáticamente las dependencias y herramientas necesarias.
   - Una vez iniciado, ingresa al directorio backend y ejecuta make run.

4. **Comandos útiles** (desde `/backend`):

   - Levantar el servidor:
     ```
     make run
     ```
   - Formatear y chequear código:
     ```
     make precommit
     ```
   - Actualizar dependencias:
     ```
     make update
     ```

5. **Endpoints principales**:

   - `GET /api/documents/list-all-documents`: Lista los documentos en el bucket GCS.
   - `POST /api/documents/upload-document`: Sube un documento PDF a GCS.
   - `POST /api/student-profile/create`: Genera un perfil estudiantil a partir de un PDF almacenado.

## Desarrollo

- El backend está en [backend/main.py](backend/main.py).
- Los servicios principales son:
  - [`GcsDocumentOperations`](backend/services/document_operations_service.py): Manejo de archivos en GCS.
  - [`AnthropicHaikuStudentProfiler`](backend/services/student_profile_service.py): Generación de perfiles con LLM.
- El prompt para el modelo está en [`prompt_templates.py`](backend/constants/prompt_templates.py).

## Licencia

Este proyecto es solo para fines educativos y de demostración.

---
