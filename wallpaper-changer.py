#!/usr/bin/python

# title           :Wallpaper-changer
# description     :This script will change the ubuntu wallpaper form live image source
# author          :Saddam H
# date            :2016-10-30
# version         :0.1
# usage           :python wallpaper-changer.py
# notes           :Follow me @thedevsaddam
# python_version  :2.6.6
# ==============================================================================

# Import essential libraries
import os
from time import sleep
from helper import log, get_max_window_size
from WallpaperManager import download_wallpaper, set_wallpaper

# set essential environment variables
os.environ['SHELL'] = '/bin/sh'
os.environ['PATH'] = '/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin'
os.environ['DISPLAY'] = ':0'

try:
    size = get_max_window_size()
    wallpaper_file_name = download_wallpaper(size[0], size[1])
    sleep(5)
    set_wallpaper(wallpaper_file_name)
except:
    log('Unable to detect maximum resolution')
    wallpaper_file_name = download_wallpaper()
    sleep(5)
    set_wallpaper(wallpaper_file_name)
