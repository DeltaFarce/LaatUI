#! /bin/bash
# Author：Laat/sunxinyang
# Created Time：2011-4-4
# Release：v1.0.0
# Script Description：

Top(){
  time=$(date "+%Y-%m-%d %H:%M:%S")
  sed -n '8,18p' | awk '{print "PID!"$2"&USER!"$3"&%CPU!"$10"&%MEM!"$11"&COMMAND!"$13"&Time!"}' &>> $(cd $(dirname $0);pwd)/top
}

while true;do
  sleep 10
  Top
done