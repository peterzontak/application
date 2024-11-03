START .\venv\Scripts\Activate
pip install -r requirements.txt
@REM python manage.py migrate
@REM python manage.py seed
@REM python manage.py collectstatic --noinput
