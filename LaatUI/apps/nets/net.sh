#! /bin/bash
# Author：Laat/sunxinyang
# Created Time：2011-4-4
# Release：v1.0.0
# Script Description：

Net(){
  RX_s=`ifconfig eth0 | grep bytes | sed -n '1p' | awk '{print $5}'`
  TX_s=`ifconfig eth0 | grep bytes | sed -n '2p' | awk '{print $5}'`
  sleep 1
  RX_end=`ifconfig eth0 | grep bytes | sed -n '1p' | awk '{print $5}'`
  TX_end=`ifconfig eth0 | grep bytes | sed -n '2p' | awk '{print $5}'`
  COUNT_RX=$(($RX_end-$RX_s))
  COUNT_TX=$(($TX_end-$TX_s))
  RX=$(echo $RX | awk '{print $COUNT_RX/50120 }')
  TX=$(echo $TX | awk '{print $COUNT_TX/50120 }')
  time=$(date "+%Y-%m-%d %H:%M:%S")
  echo -e "RX!$RX&TX!$TX&TIEM!$time" &>> $(cd $(dirname $0);pwd)/mem.html
}

while true;do
  sleep 10
  Net
done