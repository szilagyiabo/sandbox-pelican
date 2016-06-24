#!/bin/bash

docker  run  -v `pwd`:`pwd` -w `pwd` -i -t  anapsix/alpine-java sh test.sh "$1"
CONTAINER=$(docker ps -a | sed -n 2p | cut -c1-12)
docker rm $CONTAINER &> /dev/null
