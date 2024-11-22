import os
from .common import *
import dj_database_url

DEBUG = False

SECRET_KEY = os.environ['SECRET_KEY']

db_from_env = dj_database_url.parse("postgresql://storfront_owner:79PLnrHkBSFO@ep-lively-sound-a598e5ij.us-east-2.aws.neon.tech/storfront?sslmode=require")

# Update DATABASES setting with parsed database URL
DATABASES = {
    'default': db_from_env
}

ALLOWED_HOSTS = ['storefront3-wsl2.onrender.com']