#!/usr/bin/env bash
docker stop helloworld
docker rm -f helloworld
docker build . -t helloworld
docker run -d -p 5000:5000 -dit --name hw helloworld