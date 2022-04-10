#! /bin/bash
# Author：Laat/sunxinyang
# Created Time：2011-4-4
# Release：v1.0.0
# Script Description：定时清楚指定大小的日志

remove_log(){
arr_per=($(cd $(dirname $0);pwd)/apps/cpus/cpu.html $(cd $(dirname $0);pwd)/apps/dfs/df.html
  $(cd $(dirname $0);pwd)/apps/loads/load.html $(cd $(dirname $0);pwd)/apps/meninfo/mem.html
  $(cd $(dirname $0);pwd)/apps/nets/net.html  $(cd $(dirname $0);pwd)/apps/tops/top.html)

for i in $(seq 0 ${#arr_per[@]});do
  size=$(du -sm ${arr_per[$i]} | awk '{print $1}')
  if [ $size -gt 300 ];then
        rm -fr ${arr_per[$i]}
    else
        echo ${arr_per[$i]}
        echo "小于200mb"
  fi
done
}

remove_log