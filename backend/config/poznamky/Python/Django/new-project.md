1. Create && activate VENV
2. Install requiremenets
   pip install django
   pip install whitenoise
   pip install faker
   pip install gunicorn
   <!-- https://docs.allauth.org/en/latest/installation/quickstart.html#post-installation -->
   pip install django-allauth
   pip install django-extensions <!-- show_urls -->
   pip install -r .\requirements.txt
3. Start project
   django-admin startproject
4. Create app
   python ./manage.py startapp app_name
   Registered "app_name" in core/settings.py
   Registered "app_name" urls (project/app_name/urls.py -> project/core/urls.py)
5. Create Superuser
    python manage.py createsuperuser
6. Run Devserver
    python ./manage.py runserver
7. Run Tests
    python manage.py test
7. Obtain installed Django version
    python -m django --version

