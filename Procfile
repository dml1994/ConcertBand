release: sh -c 'cd ConcertBand && python manage.py migrate'
web: cd ConcertBand && gunicorn concertBand.wsgi --log-file -
