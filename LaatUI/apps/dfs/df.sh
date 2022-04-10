#! /bin/bash
# Author：Laat/sunxinyang
# Created Time：2011-4-4
# Release：v1.0.0
# Script Description：

Df(){
  df -h | sed -n '2,10p' | awk '{print "Filesystem!"$1"&Size!"$2"&Used!"$3"&Available!"$4"&Use%!"$5}' | awk '{ print $0 strftime("%Y-%m-%d
  %H:%M:%S",systime())}' &>> $(cd $(dirname $0);pwd)/df.html
}

while true;do
  sleep 10
  Df
done