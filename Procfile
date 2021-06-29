release: sh -c 'cd ConcertBand && python manage.py makemigrations  accounting && python manage.py makemigrations  app && python manage.py makemigrations registry && python manage.py migrate '
web: cd ConcertBand && gunicorn concertBand.wsgi --log-file -
