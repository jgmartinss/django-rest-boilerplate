clean:
	rm -rf config/db.sqlite3
	rm -rf config/__pycache__
	rm -rf config/settings/__pycache__
	rm -rf v1/__pycache__
	rm -rf v1/apps/__pycache__
	rm -rf v1/apps/accounts/__pycache__
	rm -rf v1/apps/accounts/migrations/*
run:
	python3 manage.py runserver
migrate:
	python manage.py migrate --run-syncdb
migrations:
	python3 manage.py makemigrations
createuser:
	python3 manage.py createsuperuser
shell:
	python3 manage.py shell
test:
	python3 manage.py test
create_requirements:
	pip3 freeze > requirements.txt
install:
	pip3 install -r requirements.txt
