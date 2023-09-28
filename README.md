# NewsApp

NewsApp is a dashboard where logged in user can view top news. Also search with previous history as well as search with keyword feature is provide.
This project is using data provided by newsapi (https://newsapi.org/).

- Python, Django, sqlite, html, css, jinja

## Step by step guide to run project

### Virtual environment
Run following command to install virtualenv.

`pip install virtualenv`

Create virtualenv

`virtualenv envname`

Activate environment

`source virtualenv_name/bin/activate`

### Install Packages
Install django

`pip install django`

Install requests

`pip install requests`

### Setup django project

Start django project

`django-admin startproject NewsApp`

create django app

`django-admin startapp news_api`

### Install requirements form requirements file

`pip install -r requirements.txt`


### Add NewsApi apikey

Get api key from NewsApi website by creating account. 
Paste that key in settings.py file.

### Run django project

Go to project folder where manage.py file is present.
`python manage.py runserver`


## Improvements 
-Better authentication - using django authentication
-Throttling 
