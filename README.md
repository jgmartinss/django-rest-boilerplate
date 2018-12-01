## Django Rest Boilerplate

> Boilerplate using Django 2 and Django REST Framework.


## Project Structure

--------

  ```sh
  . yourprojectname
  ├── config
  │   ├── __init__.py
  │   ├── environment.py
  │   ├── routes.py
  │   ├── settings
  │   │   ├── __init__.py
  │   │   ├── base.py
  │   │   ├── development.py
  │   │   └── production.py
  │   ├── urls.py
  │   └── wsgi.py
  ├── contrib
  │   └── env_gen.py
  └── v1
  ├── apps
  │   ├── accounts
  │   │   ├── __init__.py
  │   │   ├── migrations
  │   │   │   └── __init__.py
  │   │   ├── admin.py
  │   │   ├── apps.py
  │   │   ├── managers.py
  │   │   ├── models.py
  │   │   ├── serializer.py
  │   │   ├── signals.py
  │   │   └── views.py
  │   └── __init__.py
  └── __init__.py
  ├── Makefile
  ├── manage.py
  ├── Pipfile
  ├── Pipfile.lock
  ├── README.md
  ├── requirements.txt
  ├── setup.py
  ├── tox.ini
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
$ make setup
```
