#! /bin/bash
# Author：Laat/sunxinyang
# Created Time：2011-4-4
# Release：v1.0.0
# Script Description：

Mem () {
  mem_used=`head -2 /proc/meminfo | awk 'NR==1{t=$2}NR==2{f=$2;print (t-f)*100/t}'`
  mem_cache=`head -5 /proc/meminfo | awk 'NR==1{t=$2}NR==5{c=$2;print c*100/t}'`
  mem_buffer=`head -4 /proc/meminfo | awk 'NR==1{t=$2}NR==4{b=$2;print b*100/t}'`
  time=$(date "+%Y-%m-%d %H:%M:%S")
  echo -e "mem_used!$mem_used&mem_cache!$mem_cache&mem_buffer!$mem_buffer&Time!$time"
}

while true;do
  sleep 10
  Mem &>> $(cd $(dirname $0);pwd)/mem.html
done