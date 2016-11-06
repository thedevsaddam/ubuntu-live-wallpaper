#!/usr/bin/python

# title           :Wallpaper-conf
# description     :This script will set user custom configuration
# author          :Saddam H
# date            :2016-11-01
# version         :0.1
# usage           :from configManager import *
# notes           :Follow me @thedevsaddam
# python_version  :2.6.6
# ==============================================================================

# Import essential libraries
import os
from helper import base_path

categories = 'buildings,food,nature,people,technology,objects'


def set_categories(input_categories):
    """set user defined categories"""
    file_handler = open(base_path('/configs/category'), 'w')
    file_handler.write(str(input_categories))
    file_handler.close()


def get_categories():
    """Fetch user defined categories"""
    file = base_path('/configs/category')
    if not os.path.isfile(file):
        file_handler = open(file, 'w')
        file_handler.close()
    file_handler = open(file, 'r')
    stored_categories = file_handler.readline()
    file_handler.close()
    category_list = str(stored_categories).split(",")
    if bool(stored_categories):
        return category_list
    else:
        return str(categories).split(",")


def has_error(args):
    """Validate user input"""
    error_bag = []
    valid_categories = str(categories).split(",")
    for arg in args:
        if "=" in arg:
            arg_str = str(arg).split("=")
            # check category validity
            if arg_str[0] == 'category':
                input_categories = str(arg_str[1]).split(",")
                for input_cat in input_categories:
                    if input_cat not in valid_categories:
                        error_bag.append('Invalid category name ' + input_cat)
                        break

    return error_bag
