release: sh -c 'cd ConcertBand && python manage.py migrate accounting && python manage.py migrate app && python manage.py migrate registry'
web: cd ConcertBand && gunicorn concertBand.wsgi --log-file -
