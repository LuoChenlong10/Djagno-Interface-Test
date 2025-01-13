#导入公共配置
from .base import *


#开发配置
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'auto_test',
        'USER': 'root',
        'PASSWORD': 'lcl335115',
        'HOST': '127.0.0.1',
        'PORT': '3306'
    }
}
