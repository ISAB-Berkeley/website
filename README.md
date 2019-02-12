# ISAB Website 2017-2018

___

![ISAB Logo](images/logo.png "ISAB Logo")

___


## Conribute

This is the source code for the ISAB website. In order to make changes to the website first clone this repo and follow the installation directions below. Once you verify your changes locally, commit your changes and push them to this repo. You can then SSH into the web hosting account and pull the changes in order to publish them. Never modify the files directly on the web hosting machine, as we keep track of file changes using git, and test our changes before publishing them publicly.

## Installation

In order to run the website locally a MySQL development database is required.

First install the MySQL Community Server [here](https://dev.mysql.com/downloads/mysql/).

Then add `/usr/local/mysql/bin` to the `PATH` by adding the following line into your `~/.bash_profile` (this instruction assumes you are using Linux or OSX):
```
export PATH=$PATH:/usr/local/mysql/bin
```
Restart your terminal if its open for the changes to take effect.
Start the server using the command:
```
sudo /usr/local/mysql/support-files/mysql.server start
```
Connect to the mysql client using the command, and enter the default password:  
(If you forgot to note down the mysql default password follow [these steps](https://stackoverflow.com/a/22851247/3531663).)
```
mysql -u root -p
```
In the mysql terminal type the following command to create the `isab` database:
```
CREATE DATABASE isab;
```
You can now exit mysql by typing:
```
exit
```
Make sure you cloned this repo. Now head to the `isab/isab` directory and create a file called `secret.py` with contents:
```
import os

DATABASE_HOST = '127.0.0.1'
DATABASE_PORT = '3306'
DATABASE_NAME = 'isab'
DATABASE_USER = 'root'
DATABASE_PASS = 'pass'
EMAIL_USER = 'tech@isab.berkeley.edu'
EMAIL_PASS = 'pass'
S_SECRET_KEY = 'abc'
S_DEBUG = True
S_STATIC_URL = '/static/'
S_STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
S_MEDIA_ROOT = 'public/static/img/'
S_MEDIA_URL = '/public/static/img/'
S_MAINTENANCE_MODE = False
```
Make sure you update the following:
* replace `DATABASE_PASS` with your mysql password
* replace `EMAIL_PASS` with the password you find the the ISAB Tech folder on BDrive
* generate new `S_SECRET_KEY` using [this website](https://www.miniwebtool.com/django-secret-key-generator/)

You are done. Now you can go back to the Django directory (`isab`) and run:
```
pip3 install mysqlclient
pip3 install django
pip3 install django-maintenance-mode
pip3 install Pillow
python3 manage.py makemigrations
python3 manage.py makemigrations public
python3 manage.py migrate
python3 manage.py runserver
```

## Server Side

Below are some commands which can come handy when you SSH into the web hosting machine.

If you want to see the status of the ISAB website service and/or modify it, here are some useful commands:
```
systemctl --user start website
systemctl --user stop website
systemctl --user reload website
```

If the website is not starting up for some reason you can see what is wrong by viewing the logs:
```
journalctl --user -n 50
```

If `python` seems to stop working or you have to update `python` or the library versions you can delete and re-create the `venv` using the following commands:
```
rm -rf venv
virtualenv -p /usr/bin/python3 venv/
source env/bin/activate
pip install mysqlclient
pip install django
pip install django-maintenance-mode
pip install Pillow
pip install gunicorn
```

When `venv` is working properly make sure to activate it before adding/removing any libraries or using the `manage.py` command:
```
source venv/bin/activate
```

To stop using the `venv` simply type:
```
deactivate
```

## Template

This website is based on a ThemeForest template. The template can be found [here](https://themeforest.net/item/enigma-creative-responsive-minimal-html-template/12271889).
