#!/bin/bash

if [ -n "$1" ]
then
host=$1
else
host=127.0.0.1
fi

if [ -n "$2" ]
then
port=$2
else
port=8001
fi

echo $host
echo $port

RESULT=201
sleep 10
while [ $RESULT ]; do
cur_date=$(date  +%d/%b/%Y\ %H:%M:%S);
d=`grep 'cpu ' /proc/stat | awk '{usage=($2+$4)*100/($2+$4+$5)} END {print usage ""}'`
RESULT=`curl -X POST -d "date=$cur_date&cpu=$d" "http://$host:$port/add"`
sleep 10
done