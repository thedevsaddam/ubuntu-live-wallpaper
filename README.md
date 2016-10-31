# Ubuntu-live-wallpaper
Live wallpaper changer for ubuntu. Inspired from chrome momentum extension


### Installation

Open terminal ( ctrl+alt+t ) and go to __Downloads__ directory

```bash
cd ~/Downloads/
```

Clone the repository

```bash
git clone https://github.com/thedevsaddam/ubuntu-live-wallpaper.git
```
or download the zip file manually and unzip to __Downloads__ directory

Change permission to 777

```bash
sudo chmod -R 777 ubuntu-live-wallpaper
```
Open crontab in edit mode

```bash
crontab -e
```

Copy the line below and paste
```bash
*/5 * * * * python /home/YOUR_USER_NAME/Downloads/ubuntu-live-wallpaper/wallpaper-changer.py
```
Replace YOUR_USER_NAME by your user name.

_Note:  To get username type `whoami` in interminal_

The Cron job will run the script every five minutes and change the wallpaper. You can configure the Cron job to change the refresh time.
### TODO
* Change wallpaper by season
* Change wallpaper by morning, mid-day, evening and night
* Easy installation


### Credits:
* [Image source](https://source.unsplash.com)

### **License**
The **Ubuntu-live-wallpaper** is a open-source application licensed under the [MIT License](LICENSE.md).
