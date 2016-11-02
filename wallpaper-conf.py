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

# Import essential libraries
import sys
from configManager import *

args = sys.argv[1:]
if not args:
    print(
        "No argument passed!"
        "\nHelp: width=1600, height=900, category=buildings,food,nature,people,technology,objects"
    )


def validate_and_store_settings():
    """Validate the input and store settings"""

    is_input_valid = is_validate_input(args)
    if is_input_valid:
        for message in is_input_valid:
            print("Error: " + message)
        return False
    else:
        # if validation passed the store configuration
        store_configuration(args)

        # if has_input(args, 'default'):
            # if get_input(args, 'default') == 1:
            #     default_configuration()  # make default configuration


validate_and_store_settings()
