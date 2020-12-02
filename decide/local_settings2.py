ALLOWED_HOSTS = ["*"]

# Modules in use, commented modules that you won't use
MODULES = [
#    'authentication',
    'base',
    'booth',
    'census',
    'mixnet',
    'postproc',
    'store',
    'visualizer',
    'voting',
]
BASEAURL = 'http://127.0.0.1'

APIS = {
    'authentication': 'http://127.0.0.1',
    'base': 'http://127.0.0.1',
    'booth': 'http://127.0.0.1',
    'census': 'http://127.0.0.1',
    'mixnet': 'http://127.0.0.1',
    'postproc': 'http://127.0.0.1',
    'store': 'http://127.0.0.1',
    'visualizer': 'http://127.0.0.1',
    'voting': 'http://127.0.0.1',
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'HOST': 'localhost',
        'PORT': 5432,
    }
}

# number of bits for the key, all auths should use the same number of bits
KEYBITS = 256
