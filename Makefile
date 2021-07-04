.PHONY: dev-setup dev lint load-test test build run build-and-run \
        clean-fe clean-be cleanall build-frontend build-backend deploy
all: 

# === DEV RELATED ===
dev-setup:  # local dev
	poetry install
	cd frontend; npm install; cd ..

dev:
	docker-compose up -d db
	scripts/dev.sh

lint:
	-isort backend && black backend && flake8 backend
	-isort tests && black tests && flake8 tests
	cd frontend && npm run lint && cd ..

load-test:  # interactive
	locust -f tests/locustfile.py

test:  
	docker-compose up -d db
	pytest

build:
	docker-compose build

run:
	docker-compose up

build-and-run: build run

# === DOCKERFILE PRODUCTION BUILD ===
clean-fe:
	-rm -r frontend/dist

clean-be:
	-rm -r dist backend/templates backend/static

cleanall: clean-fe clean-be

build-frontend: clean-fe
	scripts/build_frontend.sh

build-backend: clean-be
	scripts/build_backend.sh

# === GCP DEPLOY ===
gcp-deploy:  # FIXME no DB access
	docker-compose build app
	# tag for us-west1 
	docker tag waypoints_app:latest us-west1-docker.pkg.dev/waypoints-demo/waypoints-demo/waypoints_app:latest
	docker push us-west1-docker.pkg.dev/waypoints-demo/waypoints-demo/waypoints_app:latest
	gcloud run deploy --image us-west1-docker.pkg.dev/waypoints-demo/waypoints-demo/waypoints_app:latest

gcp-wipe:
	gcloud artifacts repositories delete waypoints-demo --location=us-west1