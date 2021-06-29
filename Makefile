.PHONY: test lint clean run dev-setup
all: 

# === DEV RELATED ===
dev-setup:  # local dev
	poetry install
	cd fe; npm install; cd ..

dev:
	docker-compose up -d db
	scripts/dev.sh

lint:
	-isort be && black be && flake8 be
	-isort tests && black tests && flake8 tests
	cd fe && npm run lint && cd ..

load-test:  # manual test
	locust -f tests/locustfile.py

test:  # todo
	pytest

build:
	docker-compose build
run:
	docker-compose up

rebuild-and-run: build run

# === DOCKERFILE PRODUCTION BUILD ===
clean-fe:
	-rm -r fe/dist

clean-be:
	-rm -r dist be/templates be/static

cleanall: clean-fe clean-be

build-frontend: clean-fe
	scripts/build_frontend.sh

build-backend: clean-be
	scripts/build_backend.sh

