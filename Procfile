web: gunicorn FOOD_TIME.wsgi --log-file -
release: python manage.py makemigrations --noinput
release: python manage.py migrate --noinput