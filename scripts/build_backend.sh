#!/usr/bin/env bash

mkdir -p be/static/{css,js}
mkdir -p be/templates
mv fe/dist/index.html be/templates
mv fe/dist/favicon.ico be/templates
mv fe/dist/css/* be/static/css
mv fe/dist/js/* be/static/js
poetry build  # output is in dist