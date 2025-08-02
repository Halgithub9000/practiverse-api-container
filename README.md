# DIS-DCC-UdeCh-TDS.2025

Esta plantilla fue construida para el Taller de Software del Diploma de Postítulo en Ingeniería de Software utilizando el framework Django 5.x siguiendo algunas de las prácticas recomendadas en Two Scoops of Django 3.x. 

La documentación oficial de Django en conjunto con las buenas prácticas documentadas en el libro son recomendadas antes de modificar este proyecto.

Incluye la implementación completa del tutorial de django, además de una versión del mismo implementada usando class based views y endpoints de API utilizando Django RestFramework.

Puede ser utilizada como base para la construcción de los proyectos de los Equipos. 

## Requisitos

Para poder utilizar esta plantilla se recomienda tener instalado: [Docker](https://docs.docker.com/desktop/) o [Podman](https://podman-desktop.io/), [VisualStudio Code](https://code.visualstudio.com/) y [GitHub Desktop](https://desktop.github.com/download/).

Una vez clonado el repositorio, al abrirlo con VSCode, este sugerirá el uso de DevContainers y la instalación de las extensiones en la configuración incluida.

## Automatizaciones

Esta plantilla posee automatizaciones en base al uso de archivos _Makefile_. 

Estos archivo automatizan tareas comunes para el desarrollo y mantenimiento del proyecto. Cada comando puede ejecutarse con `make <comando>` desde la terminal.

### Servidor y base de datos

- **run**: inicia el servidor de desarrollo de Django en todas las interfaces (`0.0.0.0:8000`).
- **migrations**: crea nuevas migraciones para los modelos modificados y ejecuta el formateo y chequeo de calidad de código (`precommit`).
- **migrate**: aplica las migraciones pendientes a la base de datos.
- **superuser**: crea un usuario administrador para acceder al panel de Django.

### Datos de ejemplo

- **loaddata** carga datos de ejemplo desde los archivos JSON ubicados en `_fixtures/users.json` y `_fixtures/polls.json`.
- **dumpdata**: exporta los datos actuales de los modelos `users.customuser` y `polls` a archivos JSON en `_fixtures/`.

### Calidad y seguridad de código

- **precommit**: ejecuta herramientas de formateo y chequeo de calidad:
  - `isort`: ordena los imports.
  - `black`: formatea el código.
  - `flake8`: verifica estilo y errores.
  - `djlint`: formatea archivos Django templates.
- **bandit**: analiza el código en busca de vulnerabilidades de seguridad.
- **rate**: ejecuta `pylint` para analizar la calidad del código Python.
- **deadcode**: usa `vulture` para detectar código muerto (no utilizado).

### Dependencias

- **update**: actualiza las dependencias listadas en los archivos `_requirements/base.txt` y `_requirements/production.txt` usando `pur`.

### Documentación

- **docs**: genera diagramas de modelos para las apps `auth` y `polls` usando `graph_models` y los guarda en `../docs/images/`.

## Enlaces

- Python / Django: [Python 3.13](https://docs.python.org/3.13/), [Django 5.2](https://docs.djangoproject.com/en/5.2/), [WhiteNoise](https://whitenoise.readthedocs.io/en/stable/django.html), [DRF](https://www.django-rest-framework.org/), [DRF-Spectacular](https://drf-spectacular.readthedocs.io/)
- HTML / CSS / JS: [Bootstrap 5.3](https://getbootstrap.com/docs/5.3/getting-started/introduction/), [Bootstrap Icons](https://icons.getbootstrap.com/), [HTMX](https://htmx.org/docs/)
- Tutoriales: [Django Polls](https://docs.djangoproject.com/en/5.2/intro/tutorial01/), [DRF](https://www.django-rest-framework.org/tutorial/quickstart/)
