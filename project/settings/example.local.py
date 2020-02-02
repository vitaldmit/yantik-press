from .settings import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '*d0i74e_jn)z#w$fw2wxh^f$0369kyhlur_+t(lywxpd1*h!k$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
