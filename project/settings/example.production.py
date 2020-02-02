from .settings import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '*d0i74e_jn)z#w$fw2wxh^f$0369kyhlur_+t(lywxpd1*h!k$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/"version"/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': '',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

# LOGGING['handlers'].update({'logfile': {
#     'level': 'INFO',
#     'filters': ['require_debug_false'],
#     'class': 'logging.handlers.RotatingFileHandler',
#     'filename': '',  # Change this !!!
#     'maxBytes': '16777216',  # 16megabytes
#     'formatter': 'verbose'
# }})

# LOGGING['loggers']['django']['handlers'].append('logfile')
