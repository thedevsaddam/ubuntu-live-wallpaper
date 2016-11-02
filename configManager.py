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
from helper import base_path
import configparser

valid_categories = ["buildings", "food", "nature", "people", "technology", "objects"]
default_config = {
    'categories': 'buildings, food, nature, people, technology, objects',
    'width': '1600',
    'height': '900'
}


def is_validate_input(args):
    """Validate user input"""
    error_bag = []

    for arg in args:
        if "=" in arg:
            arg_str = (str(arg).split("="))
            # check the width
            if arg_str[0] == 'width':
                try:
                    val = int(arg_str[1:][0])
                except ValueError:
                    error_bag.append("Invalid screen width")

            # check the height
            if arg_str[0] == 'height':
                try:
                    val = int(arg_str[1:][0])
                except ValueError:
                    error_bag.append("Invalid screen height")

            # check category validity
            if arg_str[0] == 'category':
                input_categories = str(arg_str[1:][0]).split(",")
                categories = []

                for category in input_categories:
                    if category not in valid_categories:
                        error_bag.append('Invalid category name')
                        break

    return error_bag


def has_input(args, key):
    """Determine the key exist in input or not"""
    for arg in args:
        if "=" in arg:
            arg_str = (str(arg).split("="))
            # check the key
            if arg_str[0] == key:
                return True
            else:
                return False
    return False


def get_input(args, key):
    """get input value"""
    for arg in args:
        if "=" in arg:
            arg_str = (str(arg).split("="))
            # check the key
            if arg_str[0] == key:
                return arg_str[1]
            else:
                return None


def default_configuration():
    """Default configuration"""
    config = configparser.ConfigParser()
    config['DEFAULT'] = {'categories': default_config['categories']}
    config_file = base_path('/config.ini')
    with open(config_file, 'w') as configfile:
        config.write(configfile)


def store_configuration(args):
    """Store the user provided configuration"""

    if has_input(args, 'category'):
        category = get_input(args, 'category')
    else:
        category = get_config_categories(True)

    if has_input(args, 'width'):
        width = get_input(args, 'width')
    else:
        width = get_config_width()

    if has_input(args, 'height'):
        height = get_input(args, 'height')
    else:
        height = get_config_height()

    config = configparser.ConfigParser()
    config['DEFAULT'] = {'categories': category, 'width': width, 'height': height}
    config_file = base_path('/config.ini')
    with open(config_file, 'w') as configfile:
        config.write(configfile)


def get_configuration(key=''):
    """Fetch user configuration"""
    if not key:
        return None
    config_file = base_path('/config.ini')
    config = configparser.ConfigParser()
    config.read(config_file)
    return config['DEFAULT'][key]


def get_config_categories(raw=False):
    """Fetch categories from config"""
    raw_categories = get_configuration('categories')
    if raw:
        if raw_categories:
            return raw_categories
        else:
            return default_config['categories']

    categories = str(raw_categories).split(",")
    if categories:
        return categories
    else:
        return default_config['categories']


def get_config_width():
    """Fetch width from config"""
    if get_configuration('width'):
        return get_configuration('width')
    else:
        return 1600


def get_config_height():
    """Fetch height from config"""
    if get_configuration('height'):
        return get_configuration('height')
    else:
        return 900
