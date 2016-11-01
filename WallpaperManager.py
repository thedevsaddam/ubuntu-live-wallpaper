#!/usr/bin/python

# title           :WallpaperManager
# description     :This scripts contains wallpaper manipulation functions
# author          :Saddam H
# date            :2016-10-30
# version         :0.1
# usage           :from WallpaperManager import *
# notes           :Follow me @thedevsaddam
# python_version  :2.6.6
# ==============================================================================

# Import essential libraries
import os
import random
import urllib


def base_path(path=''):
    """Return base directory path"""
    dir_path = os.path.dirname(os.path.realpath(__file__))
    return dir_path + path


def download_wallpaper(width=1600, height=900):
    """Return the downloaded wallpaper file name"""

    # available categories
    categories = ["buildings", "food", "nature", "people", "technology", "objects"]
    category = random.choice(categories)

    # image url
    base_url = "https://source.unsplash.com"
    image_url = base_url + "/category/" + category + "/" + str(width) + "x" + str(height)

    # download image
    try:
        wallpaper_name = 'wallpaper.jpg'
        response = urllib.urlretrieve(image_url, base_path("/" + wallpaper_name))
    except:
        wallpaper_name = "default-wallpaper.jpg"  # if download failed show the default wallpaper

    return base_path("/" + wallpaper_name)


def set_wallpaper(file_name):
    """ Set wallpaper"""
    dbus_session_bus_address = "PID=$(pgrep gnome-session) && export DBUS_SESSION_BUS_ADDRESS=$(grep -z DBUS_SESSION_BUS_ADDRESS /proc/$PID/environ|cut -d= -f2-) && "
    command = dbus_session_bus_address + "gsettings set org.gnome.desktop.background picture-uri file:///" + file_name
    os.system(command)


def get_max(list_of_string):
    """Return maximum value form a list of string or integer """
    return max(map(int, list_of_string))


def get_window_size():
    """Return the window width and height"""
    width = os.popen(
        "export DISPLAY=:0 && xrandr --current | grep '*' | uniq | awk '{print $1}' | cut -d 'x' -f1").read().strip(
        "\n")
    height = os.popen(
        "export DISPLAY=:0 && xrandr --current | grep '*' | uniq | awk '{print $1}' | cut -d 'x' -f2").read().strip(
        "\n")
    if '\n' in width:
        widths = width.split('\n')
        heights = height.split('\n')
        return widths, heights
    else:
        return width, height


def get_max_window_size():
    """Return maximum resolution of connected monitors"""
    window_sizes = list(get_window_size())
    widths = []
    heights = []

    if isinstance(window_sizes[0], (list, tuple)):
        for window_size in window_sizes[0]:
            widths.append(window_size)

        for window_size in window_sizes[1]:
            heights.append(window_size)

        width = get_max(widths)
        height = get_max(heights)
    else:
        width = int(window_sizes[0])
        height = int(window_sizes[1])

    return width, height
