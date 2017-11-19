# SECURITY WARNING: don't run with debug turned on in production!

from .base import *

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1','less.tk', 'www.less.tk', 'ssel.co', 'www.ssel.co', 'blog.less.tk']
DEFAULT_REDIRECT_URL = "http://www.less.tk:8000"
PARENT_HOST = "less.tk:8000"
