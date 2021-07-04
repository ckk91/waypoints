# === BUILD FRONTEND
FROM node:lts-alpine AS fe-builder
WORKDIR /app

RUN apk add --update make bash && npm install -g @vue/cli

COPY ./scripts ./scripts
COPY Makefile Makefile
COPY frontend frontend
COPY ./scripts/vue.config.js.prod ./frontend/vue.config.js

RUN make build-frontend

# === BUILD BACKEND
FROM python:3.8.11-slim AS builder
WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends curl build-essential &&\
        curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
ENV PATH "${PATH}:/root/.poetry/bin"

COPY scripts scripts
COPY Makefile Makefile 
COPY backend backend
COPY poetry.lock poetry.lock
COPY pyproject.toml pyproject.toml

COPY --from=fe-builder /app/frontend/dist frontend/dist

RUN make build-backend

# === Execution Env
FROM python:3.8.11-slim

# logging @ GCP
ENV PYTHONUNBUFFERED True

WORKDIR /app

COPY --from=builder /app/dist/backend-*.whl .
RUN pip install backend-*.whl

EXPOSE 8000

COPY scripts/waypoint-server.sh /bin/waypoint-server

CMD ["waypoint-server"]
