#!/bin/bash

export GIT_BRANCH=$(git rev-parse --abbrev-ref HEAD)
export GIT_COMMIT=$(git rev-parse --short HEAD)

echo "GIT_BRANCH=$GIT_BRANCH" > .env
echo "GIT_COMMIT=$GIT_COMMIT" >> .env

docker compose up -d --build