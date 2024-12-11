# settings.py

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mydatabase',
        'USER': 'postgres',
        'PASSWORD': 'password',
        'HOST': 'db',  # Имя сервиса для базы данных из docker-compose.yml
        'PORT': '5432',
    }
}

# Прочие стандартные настройки Django (это не весь файл, только нужные части)
SECRET_KEY = 'fakekeyforproduction'
DEBUG = True
ALLOWED_HOSTS = ['*']
