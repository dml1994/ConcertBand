release: sh -c 'cd Concertband %% python manage.py migrate'
web: sh -c 'cd ConcertBand gunicorn concertBand.wsgi --logfile -'
