# ISAB Website 2017-2018

___

![ISAB Logo](images/logo.png "ISAB Logo")

___


## Installation

In order to run the website locally a MySQL development database is required.

First install the MySQL Community Server [here](https://dev.mysql.com/downloads/mysql/). Aim to install the MySQL version that is run on the OCF servers for consistency.

Then add `/usr/local/mysql/bin` to the `PATH` by adding the following line into your `~/.bash_profile`:
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
Now head to the `isab/isab` directory and create a file called `secret.py` with contents:
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

You are done. Now you can go back to the Django directory and run:
```
pip3 install mysqlclient
python3 manage.py makemigrations
python3 manage.py makemigrations public
python3 manage.py migrate
python3 manage.py runserver
```

## The template can be found [here](https://themeforest.net/item/enigma-creative-responsive-minimal-html-template/12271889).