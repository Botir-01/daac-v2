from decouple import config
DEBUG = config('DEBUG')

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'daac2',
        'USER': 'root',
        'PASSWORD': 'Bo977731030#',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}