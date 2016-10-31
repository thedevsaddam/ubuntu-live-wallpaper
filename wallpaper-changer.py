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

from WallpaperManager import get_max_window_size, download_wallpaper, set_wallpaper
from time import sleep

width = get_max_window_size()[0]
height = get_max_window_size()[1]

wallpaper_file_name = download_wallpaper(width, height)
sleep(1)
set_wallpaper(wallpaper_file_name)
