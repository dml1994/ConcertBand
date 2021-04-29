release: sh -c 'cd ConcertBand && python manage.py makemigration registry && python manage.py makemigration accounting && python manage.py makemigration app && python manage.py migrate'
web: sh -c 'cd ConcertBand gunicorn concertBand.wsgi --logfile -'
