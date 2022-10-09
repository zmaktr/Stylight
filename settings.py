import os
import environ

# Initialise environment variables
env = environ.Env()
environ.Env.read_env()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

INSTALLED_APPS = (    
    'app', 
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': env('NAME'),
        'USER': env('USER'),
        'PASSWORD': env('PASSWORD'),
        'HOST': env('HOST'),
        'PORT': env('PORT')
    }
}

SECRET_KEY = '4cCI6MTYzOTQ0NzgwNiwiaWF0IjofNjM5NDQ3ODA2fQ' 