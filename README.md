# Lairn — Sistema Adaptativo de Aprendizaje

> API backend para una plataforma de tutoría inteligente que genera exámenes adaptativos con IA y modela el conocimiento del estudiante en tiempo real.

---

## Índice de Documentación

| Documento | Descripción |
|-----------|-------------|
| [Arquitectura del Sistema](docs/arquitectura.md) | Stack tecnológico, estructura de carpetas y diagrama de apps |
| [Autenticación y Usuarios](docs/autenticacion.md) | Registro, login, JWT, roles y permisos |
| [Cursos y Exámenes](docs/cursos-examenes.md) | Gestión de cursos, inscripciones y configuración de exámenes |
| [Motor Adaptativo](docs/motor-adaptativo.md) | Motor de IA, sesiones, ajuste de dificultad y modelo de conocimiento |
| [Analítica y Reportes](docs/analitica.md) | Resultados, avances, patrones y resúmenes por curso |
| [Referencia de la API](docs/api-referencia.md) | Todos los endpoints, métodos, parámetros y ejemplos |
| [Variables de Entorno](docs/variables-entorno.md) | Configuración de entorno y secretos |
| [Despliegue con Docker](docs/despliegue.md) | Configuración Docker, Docker Compose y producción |

---

## Vista Rápida

```
Rol: Docente                  Rol: Estudiante
──────────────────            ──────────────────
1. Crea un curso              1. Se inscribe al curso
2. Crea un examen             2. Inicia el examen
3. Consulta analítica         3. Responde preguntas IA
                              4. Recibe resultado y nota
```

### Stack Principal

| Tecnología | Versión | Uso |
|------------|---------|-----|
| Python | 3.12 | Lenguaje base |
| Django | 6.0.4 | Framework web |
| Django REST Framework | 3.17.1 | API REST |
| PostgreSQL | 16 | Base de datos |
| Claude Haiku | 4.5 | Generación de preguntas IA |
| SimpleJWT | 5.5.1 | Autenticación JWT |
| Docker / Compose | latest | Contenedorización |

---

## Inicio Rápido

### Con Docker (recomendado)

```bash
# 1. Clonar el repositorio
git clone <url-repositorio>
cd backend_lairn

# 2. Configurar variables de entorno
cp .env.example .env
# Editar .env con tus valores (especialmente ANTHROPIC_API_KEY)

# 3. Levantar servicios
docker-compose up --build

# 4. La API estará disponible en:
# http://localhost:8000/api/
```

### Sin Docker

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py seed_roles
python manage.py seed_usuarios
python manage.py runserver
```

---

## Documentación Interactiva

Una vez el servidor esté corriendo:

| URL | Descripción |
|-----|-------------|
| `http://localhost:8000/api/docs/` | Swagger UI |
| `http://localhost:8000/api/redoc/` | ReDoc |
| `http://localhost:8000/api/schema/` | OpenAPI 3.0 (JSON) |

---

## Usuarios de Prueba

Creados por `python manage.py seed_usuarios`:

| Email | Contraseña | Rol |
|-------|-----------|-----|
| `admin@pseudotutor.com` | `admin1234` | Administrador |
| `docente@pseudotutor.com` | `docente1234` | Docente |
| `estudiante@pseudotutor.com` | `estudiante1234` | Estudiante |

---

## Estructura del Proyecto

```
backend_lairn/
├── README.md                    ← Este archivo
├── docs/                        ← Documentación detallada
│   ├── arquitectura.md
│   ├── autenticacion.md
│   ├── cursos-examenes.md
│   ├── motor-adaptativo.md
│   ├── analitica.md
│   ├── api-referencia.md
│   ├── variables-entorno.md
│   └── despliegue.md
├── manage.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── backend_lairn/               ← Configuración Django
├── core/                        ← Utilidades compartidas
└── apps/                        ← Módulos de negocio
    ├── users/
    ├── examenes/
    ├── motor_adaptativo/
    ├── analitica/
    └── moderacion/
```

---

*Lairn — Adaptive Learning API · Django 6 · Python 3.12 · PostgreSQL 16 · Claude AI*
