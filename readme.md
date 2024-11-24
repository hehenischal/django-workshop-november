# Project Setup
django-admin startproject my_project
cd my_project
python manage.py startapp my_app

# Run Development Server
python manage.py runserver

# Database Management
python manage.py migrate
python manage.py makemigrations my_app
python manage.py migrate

# Admin Interface
python manage.py createsuperuser

# Shell Access
python manage.py shell

# Testing
python manage.py test

# Additional Commands
python manage.py collectstatic
python manage.py check --deploy
python manage.py check --list-installed-apps
python manage.py inspectdb
