Django Excel Processer
=

This is a test assignment.

# Task:
>На вход : эксель с рекламной компанией.
 В интерфейсе появляются заголовок и текст объявления (только те объявления у которых стоит статус смена объявления "да")
 меняется заголовок и текст объявления, нажимается кнопка сохранить
 Обновляется эксель с объявлениями и выгружается (скачивается по кнопке "загрузить обновленный эксель")


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
1. load properly formatted xls file or example from sample file folder
2. edit fields in edit form
3. press "Сохранить данные" button to save changes
4. press "Скачать обновленный эксель" to download updated xls file

# Screenshots:

![1](https://github.com/ADemkin/django-xlsx-form-processer/raw/master/screenshots/1.png)
![2](https://github.com/ADemkin/django-xlsx-form-processer/raw/master/screenshots/2.png)

&copy; Anton Demkin, 2018

antondemkin@yandex.ru
