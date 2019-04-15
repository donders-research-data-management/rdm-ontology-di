#!/bin/bash
if [ -z "$1" ]; then
  echo Updating from tag release
else
  export TAG="$1"
  echo Updating from tag "$1"
fi
docker-compose pull
docker-compose up -d
