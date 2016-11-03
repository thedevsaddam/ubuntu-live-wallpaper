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
from configManager import set_categories, has_error

args = sys.argv[1:]
if not args:
    print(
        "No argument passed!"
        "\nHelp:Provide any category you want. category=buildings,food,nature,people,technology,objects"
    )


def validate_and_store_settings():
    """Validate the input and store settings"""
    error_messages = has_error(args)

    if args and "=" in args[0]:
        if error_messages:
            for message in error_messages:
                print("Error: " + str(message))
            return False
        else:
            # if validation passed the store configuration
            categories = str(args[0]).split("=")[1]
            set_categories(categories)
            print("Configuration saved successfully!\n")


validate_and_store_settings()
