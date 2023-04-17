Create Django Meetup Application

Some steps to start in ubuntu based linux

1. sudo dnf install -y python3
2. sudo dnf install -y python3-virtualenv.noarch
3. cd django-meetup
4. mkdir venv
5. python -m venv venv
6. source /venv/bin/activate
7. pip install -r requirement.txt
8. python manage.py makemigrations
9. python manage.py migrate
10. python manage.py createsuperuser
11. python manage.py runserver
12. deactivate after done with work
