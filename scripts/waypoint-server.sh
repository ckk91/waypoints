#!/usr/bin/env bash

gunicorn -w 4 -k uvicorn.workers.UvicornWorker be.app:app --bind 0.0.0.0:8000