#!/usr/bin/python

# title           :Wallpaper-conf
# description     :This script will set user custom configuration
# author          :Saddam H
# date            :2016-11-01
# version         :0.1
# usage           :python wallpaper-conf.py
# notes           :Follow me @thedevsaddam
# python_version  :2.6.6
# ==============================================================================

import sys

args = sys.argv[1:]
if not args:
    print(
        "No argument passed!"
        "\nHelp: screen-width=1600, screen-height=1600, category=buildings,food,nature,people,technology,objects"
    )

file_handler = open('db', 'w')
file_handler.write(str(args))
file_handler.close()
