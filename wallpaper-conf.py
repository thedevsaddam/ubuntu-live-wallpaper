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
from configManager import set_categories, has_error, set_tags

args = sys.argv[1:]
if not args:
    print(
        "No argument passed!"
        "\nHelp:Provide any category you want. category=buildings,food,nature,people,technology,objects\ntag=mac,ipad"
    )


def validate_and_store_settings():
    """Validate the input and store settings"""
    error_messages = has_error(args)

    for arg in args:
        if "=" in arg:
            str_arg = (str(arg)).split("=")
            input_type = str_arg[0]
            input_value = str_arg[1]
            if input_type == "category":
                if error_messages:
                    for message in error_messages:
                        print("Error: " + str(message))
                    return False
                else:
                    # if validation passed the store configuration
                    set_categories(input_value)

            if input_type == "tag":
                set_tags(input_value)

    print("Configuration saved successfully!\n")


validate_and_store_settings()
