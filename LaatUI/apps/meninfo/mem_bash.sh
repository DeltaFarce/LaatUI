#! /bin/bash
# Author：Laat/sunxinyang
# Created Time：2011-4-4
# Release：v1.0.0
# Script Description：

tail -n 60 $(cd $(dirname $0);pwd)/mem.html &> $(cd $(dirname $0);pwd)/mem_bash.html