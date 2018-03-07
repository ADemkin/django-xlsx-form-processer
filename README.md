Django Excel Processer
=

This is a test assignment.

# How to install

Python3 is required.

1. Clone this repository
2. (optional) create virtual enviroment
3. install packages from requirements.txt
4. create .env file

```
git clone https://github.com/ADemkin/django-xlsx-form-processer.git
cd django-xlsx-form-processer
pip3 install -r requirements.txt
touch main/.env
nano main/.env
```

Paste this into your .env file: 
```
SECRET_KEY = 'n3^d7z$d_0r7-i84@g_#3o^rfg9yg7k0wg$hqjvxf0glhkrdo8'
DEBUG = True
```
Ctrl + O, Enter to write file. Ctrl + x to exit Nano.

Finally, make migration to create database required for django to operate.
```
python3 manage.py migrate
```

# Run project:
When in project folder run:
```
python3 manage.py runserver
```
Go to your browser and visit [local server](http://127.0.0.1:8000/)

# Usage:
1. load properly formatted xls file
2. edit fields in edit form
3. press "Save Fields' button to save changes
4. press "Download Updated File" to download updated xls file

&copy; Anton Demkin, 2018

antondemkin@yandex.ru
