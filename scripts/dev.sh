#!/usr/bin/env bash

pushd frontend
npm run serve &
popd

# uvicorn for local development
uvicorn backend.app:app --reload