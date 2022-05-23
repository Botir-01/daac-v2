from decouple import config
DEBUG = config('DEBUG') == 'False'

ALLOWED_HOSTS = ['backend.daac.uz']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': config("NAME"),
        'USER': config("USER"),
        'PASSWORD': config('PASSWORD'),
        'HOST': config("HOST"),
        'PORT': config('PORT'),
    }
}