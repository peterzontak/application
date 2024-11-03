## Migrate 
python manage.py migrate
python manage.py seed

## Build Assets
npm run build-prod

## Collect static
python manage.py collectstatic --noinput

# toto moze byt pain, lebo on ma jednoduchsiu folder structuru - bez 2x django/django
gunicorn django.wsgi

