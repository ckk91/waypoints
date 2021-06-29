# Waypoints CRUD
WIP - Demonstrating ability to move data from frontend to backend and vice-versa

## Quickstart
- `docker-compose up`, or `make run` then open localhost:8000 in the browser
- API docs are at `localhost:8000/docs`


## dev requirements
- poetry
- python >3.8
- vue-cli
- docker-(compose)
## Contribute
- entrypoint is makefile
- `make lint` to autoformat backend and frontend
- `make load-test` for simple backend load-testing facilities provided by locusts

TODO tests
### local dev setup
- `make dev-setup`, given the requirements are fulfilled
### local dev
- `poetry shell` to activate venv
- `make dev` to bring up the dev env (todo fix db race condition)
  - backend and frontend have their own development servers. ports are shown via cli
- `make test` to run tests via pytest


---------------
