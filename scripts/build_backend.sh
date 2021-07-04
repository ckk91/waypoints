#!/usr/bin/env bash

mkdir -p backend/static/{css,js}
mkdir -p backend/templates
mv frontend/dist/index.html backend/templates
mv frontend/dist/favicon.ico backend/templates
mv frontend/dist/css/* backend/static/css
mv frontend/dist/js/* backend/static/js
poetry build  # output is in dist