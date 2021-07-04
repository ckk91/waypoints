# Waypoints CRUD
A small service demonstrating moving data from frontend to backend and vice-versa.
Built from scratch (except frontend via vue-cli) with Python 3, fastapi+uvicorn+uvloop, SQLAlchemy, VueJS, Bootstrap and Postgres. 

Find details about technical decisions in [DECISIONS.md](./DECISIONS.md).

![Screenshot of the UI](./img/demo.png?raw=true "The UI in use")

Table of Contents
=================
- [Waypoints CRUD](#waypoints-crud)
- [Table of Contents](#table-of-contents)
  - [Quickstart](#quickstart)
  - [(Local) dev requirements](#local-dev-requirements)
  - [Development](#development)
    - [Local dev setup](#local-dev-setup)
    - [Local dev](#local-dev)
  - [TODO](#todo)


## Quickstart
- `docker-compose up`, or `make run` then open localhost:8000 in the browser once the service has been created.
- API docs are at `localhost:8000/docs`
- Enter a waypoint as a comma separated string and click save
- See it pop up in the table below!

## (Local) dev requirements
- python >=3.8
- docker-(compose)
- node >= 10.19
- vue-cli https://cli.vuejs.org/
- poetry https://python-poetry.org/
- make https://www.gnu.org/software/make/

## Development
### Local dev setup
- Entrypoint for mostly everything is the Makefile
- `make dev-setup`, given the requirements are fulfilled

### Local dev
- `poetry shell` to activate the projects virtual environment
- `make dev` to bring up the development servers
  - backend and frontend have their own development servers. ports are shown via cli
- `make test` to run tests via pytest
- `make lint` to lint and autoformat backend and frontend
- `make load-test` for simple backend load-testing facilities provided by locust.

## TODO
- [ ] Configure for GCP Cloud run
- [ ] fix dev env race condition