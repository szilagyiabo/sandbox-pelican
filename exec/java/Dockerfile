FROM alpine

ENV JAVAFILE=Main.java

RUN apk --update add openjdk7-jre

RUN touch run.sh
RUN echo "#!/bin/sh" >> run.sh
RUN echo "" >> run.sh
RUN echo "file=$JAVAFILE" >> run.sh
RUN echo "javac \"$file\"" >> run.sh
RUN echo "java \"${file%.*}\"" >> run.sh

CMD ["/bin/sh"]
