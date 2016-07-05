#!/bin/sh

FILENAME=$1
EXTENSION=`echo $FILENAME | awk -F. '{ print "."$NF }'`
RUNNABLE=`echo $(basename $FILENAME) | awk -F$EXTENSION '{ print $1 }'`
chmod 777 $FILENAME
javac $FILENAME
cd $(dirname $FILENAME) && java $RUNNABLE
