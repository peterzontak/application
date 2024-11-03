# Basic Commands

## build
docker-compose up -d --build
## build no cache
docker-compose up --force-recreate

## list all running
docker ps -a

docker-compose down

## stop
docker ps -q | ForEach-Object { docker stop $_ }

## remove all containers
docker ps -a -q | ForEach-Object { docker rm $_ }

## Stop and remove all containers
docker ps -q | ForEach-Object { docker stop $_ } | docker ps -a -q | ForEach-Object { docker rm $_ }

## remove all images
docker image prune -a

## Remove unused images
docker images -q --filter "dangling=false" | ForEach-Object { docker rmi $_ }
docker images -q | Where-Object { $_ -ne (docker images -q redis:7.4-alpine) } | ForEach-Object { docker rmi $_ }

## Remove all volumes
docker volume ls -q | ForEach-Object { docker volume rm $_ }

## remove everything
docker ps -q | ForEach-Object { docker stop $_ } | docker ps -a -q | ForEach-Object { docker rm $_ } | docker images -q | Where-Object { $_ -ne (docker images -q redis:7.4-alpine) } | ForEach-Object { docker rmi $_ }


## REMOVE BUILD CACHE
docker builder prune -a



# Python

## interactive console
docker exec -it django /bin/sh


## interactive python console
python manage.py shell



# Celery

# Test Celery tasks
from newapp.tasks import sharedtask
sharedtask.delay()

from celeryworker.celerytask import add_numbers
add_numbers.delay()



