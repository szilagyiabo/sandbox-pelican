docker  run  -v `pwd`:`pwd` -w `pwd` -i -t  szilagyiabo/alpine-gcc sh testProgram.sh
CONTAINER=$(docker ps -a | sed -n 2p | cut -c1-12)
docker rm $CONTAINER &> /dev/null
