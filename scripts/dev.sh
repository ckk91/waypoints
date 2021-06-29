#!/usr/bin/env bash

pushd fe
npm run serve &
popd
#pushd be
uvicorn be.app:app --reload