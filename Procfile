release: sh -c 'cd ConcertBand %% python manage.py migrate'
web: sh -c 'cd ConcertBand gunicorn concertBand.wsgi --logfile -'
