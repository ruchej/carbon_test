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

sh demon.sh $host $port |
python3 manage.py runserver $host:$port