#!/bin/bash

project=animal_noises

#build server
docker build -t ${project}_server server

#build animal_api
docker build -t ${project}_api animal_api

#Create network
docker network create ${project}_network

#Run containers
docker run -d \
    -p 5000:5000 \
    --name ${project}_server \
    --network ${project}_network \
    ${project}_server

docker run -d \
    --name ${project}_api \
    --network ${project}_network \
    ${project}_api