import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

INSTALLED_APPS = (    
    # 'django.contrib.contenttypes',
    'app', 
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'stylight',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': 'localhost',
        'PORT': '3306'
    }
}

SECRET_KEY = '4cCI6MTYzOTQ0NzgwNiwiaWF0IjofNjM5NDQ3ODA2fQ' 