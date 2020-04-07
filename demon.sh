#!/bin/bash

RESULT=201
sleep 10
while [ $RESULT ]; do
cur_date=$(date  +%d/%b/%Y\ %H:%M:%S);
d=`grep 'cpu ' /proc/stat | awk '{usage=($2+$4)*100/($2+$4+$5)} END {print usage ""}'`
RESULT=`curl -X POST -d "date=$cur_date&cpu=$d" 'http://localhost:8000/add'`
sleep 10
done