## Django Rest Boilerplate

> Boilerplate using Django 2 and Django REST Framework.


## Project Structure

--------

  ```sh
  . yourprojectname
  ├── config
  │  ├── environment.py
  |  ├── settings_base.py
  |  ├── settings_local.py          
  |  ├── urls.py
  |  ├── wsgi.py
  │  └── __init__.py                
  ├── v1                    
  ├────── apps
  ├──────── accounts
  ├──────── __init__.py
  ├────── __init__.py
  ├── __init__.py
  ├── gitignore.py
  ├── makefile
  ├── README.md
  ├── manage.py
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
$ make makemigrations
$ make migrate
$ make user
$ make run
```
