#!/usr/bin/env bash
# PORT var for GCP/Heroku
gunicorn -w "${BE_WORKERS:-1}" -k uvicorn.workers.UvicornWorker backend.app:app --bind :"${PORT:-8000}"