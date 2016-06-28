#!/bin/bash

docker  run  -v `pwd`:`pwd` -w `pwd` -i -t  szilagyiabo/alpine-python python test.py
CONTAINER=$(docker ps -a | sed -n 2p | cut -c1-12)
docker rm $CONTAINER &> /dev/null
