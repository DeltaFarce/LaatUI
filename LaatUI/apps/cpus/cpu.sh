#! /bin/bash
# Author：Laat/sunxinyang
# Created Time：2011-4-4
# Release：v1.0.0
# Script Description：
Cpu(){
  top -n 1 | sed -n '3p' | awk '{print "US!"$2"&SY!"$4"&Free!"$8"&Time!"}' | awk '{ print \
  $0 strftime("%Y-%m-%d %H:%M:%S",systime())}'  &>> $(cd $(dirname $0);pwd)/top.html
}

while true;do
  sleep 10
  Cpu
done