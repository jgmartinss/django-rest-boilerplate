## Django Rest Boilerplate

> Boilerplate using Django 2 and Django REST Framework.


## Project Structure

--------

  ```sh
  . yourprojectname
  ├── config
  |  ├── environment.py      
  |  ├── urls.py
  |  ├── wsgi.py
  │  └── __init__.py                
  ├───── settings
  │     ├── base.py
  |     ├── development.py
  |     ├── production.py   
  │     └── __init__.py   
  ├── v1                    
  ├────── apps
  ├──────── accounts
  ├──────── __init__.py
  ├────── __init__.py
  ├── __init__.py
  ├── gitignore.py
  ├── Makefile
  ├── manage.py
  ├── README.md
  └── requirements.txt
  ```

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

$ make install
```

Initialize project:
```sh
$ make migrations
$ make migrate
$ make createuser
$ make run
```
