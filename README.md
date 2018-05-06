## Django Rest Boilerplate

> Boilerplate using Django 2 and Django REST Framework.


### Project Structure

  . yourprojectname
  ├── config                
  ├── v1                    
  ├────── apps
  ├──────── accounts
  ├──────── __init__.py
  ├────── __init__.py
  ├── __init__.py
  ├── gitignore.py
  ├── README.md
  ├── manage.py
  └── requirements.txt

## Let's use!

Cloning the repository in your virtualenv:

```sh
$ cd your-virtualenv

$ source bin/activate

$ git clone https://github.com/jgmartinss/django-rest-boilerplate.git yourprojectname
```

Install required packages:

```sh
$ cd yourprojectname

$ pip3 install -r requirements.txt
```

Initialize project:
```sh
$ python3 manage.py makemigrations
$ python3 manage.py migrate
$ python3 manage.py createsuperuser
$ python3 manage.py runserver
```

