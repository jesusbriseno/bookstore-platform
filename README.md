## Auditoria de dependencias

La auditoria de dependencias se ejecuta automaticamente en el pipeline CI mediante:

poetry run pip-audit

Esto garantiza que no existan vulnerabilidades conocidas en las dependencias del proyecto.

## Observabilidad

El sistema incluye:

- Logging estructurado
- Middleware de registro de requests
- Manejo centralizado de errores
- Diferenciación de niveles: INFO, WARNING, ERROR

## Rendimiento

- Soporte de paginación (limit, offset)
- Diseño desacoplado para escalabilidad
- Imagen Docker optimizada (python:slim)

# Bookstore API
Servicio backend desarrollado con FastAPI aplicando Arquitectura Hexagonal (Ports & Adapters) y principios de Clean Architecture.

---

## Arquitectura

El proyecto sigue Arquitectura Hexagonal:

            ┌───────────────┐
            │   FastAPI     │
            │   (API Layer) │
            └───────┬───────┘
                    │
            ┌───────▼───────┐
            │ Application   │
            │ (Services)    │
            └───────┬───────┘
                    │
            ┌───────▼───────┐
            │ Domain        │
            │ Entities &    │
            │ Ports         │
            └───────┬───────┘
                    │
        ┌───────────▼───────────┐
        │ Infrastructure        │
        │ SQL / InMemory        │
        └───────────────────────┘

---

## Tecnologías

- Python 3.13
- FastAPI
- SQLAlchemy 2.0
- Alembic
- Poetry
- Pytest
- Ruff / Black / MyPy
- Docker
- GitHub Actions CI

---

## Seguridad

- Autenticación JWT
- Manejo estandarizado de errores
- Docker ejecutándose como usuario no root
- Auditoría automática de dependencias con `pip-audit` en CI

---

## Observabilidad

- Logging estructurado
- Middleware de registro de requests
- Manejo centralizado de excepciones

---

## Rendimiento

- Soporte de paginación (`limit`, `offset`)
- Diseño desacoplado para escalabilidad
- Imagen Docker optimizada (`python:slim`)

---

## Testing

Tipos de pruebas:

- Unit tests (Service Layer)
- Integration tests (FastAPI + TestClient)

Ejecutar:
