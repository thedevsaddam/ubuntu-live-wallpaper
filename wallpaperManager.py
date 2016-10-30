#!python

import os
import random
import urllib
from time import sleep

# available categories
categories = ["buildings", "food", "nature", "people", "technology", "objects"]
category = random.choice(categories)

# image url
baseUrl = "https://source.unsplash.com"
imageUrl = baseUrl + "/category/" + category + "/1600x900"

# current directory
dirPath = os.path.dirname(os.path.realpath(__file__))

# download image
try:
    wallpaperName = 'wallpaper.jpg'
    response = urllib.urlretrieve(imageUrl, dirPath + "/" + wallpaperName)
except:
    wallpaperName = "default-wallpaper.jpg"  # if download failed show the default wallpaper

# pause for sometime
sleep(1)

# change wallpaper using shell command
DBUS_SESSION_BUS_ADDRESS = "PID=$(pgrep gnome-session) && export DBUS_SESSION_BUS_ADDRESS=$(grep -z DBUS_SESSION_BUS_ADDRESS /proc/$PID/environ|cut -d= -f2-) && "
command = DBUS_SESSION_BUS_ADDRESS + "gsettings set org.gnome.desktop.background picture-uri file:///" + dirPath + "/" + wallpaperName
os.system(command)
