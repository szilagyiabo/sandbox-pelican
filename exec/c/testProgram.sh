#!/bin/sh

chmod 777 $1
gcc -o out $1
./out
