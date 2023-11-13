import os
from .default import *

SECRET_KEY = os.getenv('SECRET_KEY', 'django-insecure-4_w49d095w%5h60yzvr8hx5v=vp^+b*5r8ll@)7n$ivfy#se=q')

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'authentication',
    'labels',
    'colorfield',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
