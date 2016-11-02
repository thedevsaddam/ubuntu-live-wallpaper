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
from helper import base_path
from configManager import is_validate_input, store_configuration, get_configuration

args = sys.argv[1:]
if not args:
    print(
        "No argument passed!"
        "\nHelp: width=1600, height=900, category=buildings,food,nature,people,technology,objects"
    )

is_validate_input(args)
# print(get_configuration('categories'))
