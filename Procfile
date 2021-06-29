release: sh -c 'cd ConcertBand && python manage.py migrate accounting app registry'
web: cd ConcertBand && gunicorn concertBand.wsgi --log-file -
