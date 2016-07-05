FROM alpine

RUN apk add --no-cache g++
RUN apk add --no-cache make

COPY ./testProgram.sh /usr/local/bin/runGccCode
RUN chmod 755 /usr/local/bin/runGccCode

CMD ["/bin/sh"]
