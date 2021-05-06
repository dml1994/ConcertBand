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

KEYBITS = 256
