ALLOWED_HOSTS = ["*"]

MODULES = [
    'app',
    'accounting',
    'registry',
]

APIS = {
    'app':'http://localhost:8000',
    'accounting':'http://localhost:8000',
    'registry':'http://localhost:8000',
}

BASEURL = 'http://localhost:8000'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env('POSTGRESQL_NAME'),
        'USER': env('POSTGRESQL_USER'),
        'PASSWORD': env('POSTGRESQL_PASS'),
        'HOST': env('POSTGRESQL_HOST'),
        'PORT': env('POSTGRESQL_PORT'),
    }
}

KEYBITS = 256
