#! /bin/bash
# Author：Laat/sunxinyang
# Created Time：2011-4-4
# Release：v1.0.0
# Script Description：

tail -n 60 $(cd $(dirname $0);pwd)/cpu.html &> $(cd $(dirname $0);pwd)/cpu_bash.html