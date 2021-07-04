# Design Decisions
- [Design Decisions](#design-decisions)
  - [Architecture](#architecture)
  - [Environment](#environment)
    - [Build](#build)
  - [Backend](#backend)
    - [Server](#server)
    - [Database](#database)
  - [Frontend](#frontend)

## Architecture
- Application is currently configured to run as a monolith in a single container, but can be easily split up into a (statically) served frontend and respective backend parts. No real business logic layer necessary at the moment.

## Environment
- Makefile serves as an abstraction layer and overarching entry point for dev, build, run. Wrapper around (shell) scripts.

### Build
- multi stage docker file for building to keep final image small
- `.docker` dir to keep environment related files sorted
- docker-compose file w/ app and db(postgres) services
- environment vars are injected during runtime per `.env`

## Backend
- Python 3, fastapi+uvicorn, SQLAlchemy, gunicorn
- fastapi: JSON-first, automagic api docs via OpenAPI and overall very flask-like. perfect for microservices
- poetry as package management and python-specific build tool
- app utilizes a builder pattern to reify the creation and make it reusable in other modules. E.g. tests.
- tests via pytest
- simple load testing with locust
- formatted and linted with black, flake8, isort. No point in wasting time about code style
- pagination is hard-limited by env var to avoid clogging the service by dumping the whole db
- waypoint input gets parsed and cleaned on server side
- Switched over to uvicorn uvloop after initial load test via locust
- After load test: Rewrote the api to use async functions
- result of async conversion: 1000 locust users ok, no app breakdown like with pre-async on wsl2 ubuntu with consumer grade hardware.

### Server
- Chose Gunicorn as a robust production-grade (a)wsgi server
- UI and API are served via Gunicorn running uvicorn async workers.

### Database 
- Postgres, data never stays non-relational
- Sqlalchemy as ORM

## Frontend
- VueJS via vue-cli. Quick and pragmatic solution that works.
- Bootstrap-vue for fast scaffolding
- axios for xhr requests
- natural input: lat long as comma separated form, parsed in backend
- Bulk retrieval: Table is getting its current view data via api call on click of pagination widget
- 
