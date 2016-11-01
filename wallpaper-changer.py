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

from WallpaperManager import base_path, get_max_window_size, download_wallpaper, set_wallpaper
from time import sleep

try:
    size = get_max_window_size()
    wallpaper_file_name = download_wallpaper(size[0], size[1])
    sleep(10)
    set_wallpaper(wallpaper_file_name)
except Exception as e:
    file_handler = open(base_path('/ubuntu-live-wallpaper.log'), 'w')
    file_handler.write(str(e.message))
    file_handler.close()
finally:
    wallpaper_file_name = download_wallpaper(size[0], size[1])
    sleep(10)
    set_wallpaper(wallpaper_file_name)
