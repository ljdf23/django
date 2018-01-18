from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('DJANGO_SECRET_KEY', default='ln3w@psna25zxfa=^kraf*r@=$$(sol+%(a4+n^lphb=99w1^w')

DEBUG = env.bool('DJANGO_DEBUG', default=True)