#!/usr/bin/env sh

##############################################################################
##
##  Stop and kill currently running docker image, pull newest version and
##  run it.
##
##############################################################################

warn ( ) {
    echo "$*"
}

warn "Currently running docker images"
docker ps -a

warn "Killing currently running docker image..."
docker kill potic-pocket-api; docker rm potic-pocket-api

warn "Pulling latest docker image..."
docker pull potic/potic-pocket-api:$TAG_TO_DEPLOY

warn "Starting docker image..."
docker run -dit --name potic-pocket-api --restart on-failure -e POCKET_APP_KEY=$POCKET_APP_KEY -e ENVIRONMENT_NAME=$ENVIRONMENT_NAME -p 40403:5000 potic/potic-pocket-api:$TAG_TO_DEPLOY

warn "Currently running docker images"
docker ps -a
