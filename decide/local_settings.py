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
BASEURL = 'http://localhost:8006'

APIS = {
    'authentication': 'http://localhost:8006',
    'base': 'http://localhost:8006',
    'booth': 'http://localhost:8006',
    'census': 'http://localhost:8006',
    'mixnet': 'http://localhost:8006',
    'postproc': 'http://localhost:8006',
    'store': 'http://localhost:8006',
    'visualizer': 'http://localhost:8006',
    'voting': 'http://localhost:8006',
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'test_decide',
        'USER': 'decide',
	'PASSWORD': 'decide',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

# number of bits for the key, all auths should use the same number of bits
KEYBITS = 256
