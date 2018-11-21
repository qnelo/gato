create environment

`python3 -m venv django-env`

activate environment

`. django-env/bin/activate`

install django

`pip install django`

django-admin startproject gato

run server

`python ./monedas/manage.py runserver`

crear aplicacion

python ./monedas/manage.py startapp player

migraciones

python monedas/manage.py makemigrations
python monedas/manage.py sqlmigrate dolar 0001
python monedas/manage.py migrate
python monedas/manage.py showmigratios

ver sql migration

python monedas/manage.py sqlmigrate appname migrationname

crear superuser

`python ./monedas/manage.py createsuperuser`