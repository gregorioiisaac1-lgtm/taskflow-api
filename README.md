# taskflow-api
# TaskFlow API 🚀

Una API RESTful construida con FastAPI y Python para la gestión de proyectos y tareas. Este proyecto implementa un sistema CRUD completo con persistencia de datos, diseñado con arquitectura modular y validación estricta.

## Tecnologías Utilizadas
* **Framework:** FastAPI
* **Base de Datos:** SQLite
* **ORM:** SQLAlchemy
* **Validación de Datos:** Pydantic
* **Servidor ASGI:** Uvicorn

## Características Principales
* **CRUD Completo:** Creación, lectura, actualización y eliminación de tareas.
* **Persistencia Local:** Almacenamiento seguro mediante SQLite (`tasks.db`).
* **Inyección de Dependencias:** Manejo eficiente de sesiones de base de datos por cada petición HTTP.
* **Validación Automática:** Tipado estricto de esquemas de entrada y salida con Pydantic.
* **Documentación Interactiva:** Interfaz autogenerada (Swagger UI) para pruebas en tiempo real.

## Instalación y Configuración (Entorno Linux / WSL)

1. Clona el repositorio:
   ```bash
   git clone [https://github.com/tu-usuario/taskflow-api.git](https://github.com/tu-usuario/taskflow-api.git)
   cd taskflow-api