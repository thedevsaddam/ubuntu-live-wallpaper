#!/usr/bin/python

# title           :WallpaperManager
# description     :This script will change the ubuntu wallpaper form live image source
# author          :Saddam H
# date            :2016-10-30
# version         :0.1
# usage           :python wallpaperManager.py
# notes           :Follow me @thedevsaddam
# python_version  :2.6.6
# ==============================================================================

from WallpaperManager import get_window_size, download_wallpaper, set_wallpaper
from time import sleep

extra_pixels = 200
window_width = get_window_size()[0] + extra_pixels
window_height = get_window_size()[1] + extra_pixels

wallpaper_file_name = download_wallpaper(window_width, window_height)

sleep(2)

set_wallpaper(wallpaper_file_name)
