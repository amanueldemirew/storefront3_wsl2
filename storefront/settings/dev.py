from .common import *
import dj_database_url

DEBUG = True

SECRET_KEY = 'django-insecure-hs6j037urx6iav+7#10%-vu4l4f5@@-1_zo)oft4g7$vf2$jmp'

# Parse the database URL
db_from_env = dj_database_url.parse("postgresql://storfront_owner:79PLnrHkBSFO@ep-lively-sound-a598e5ij.us-east-2.aws.neon.tech/storfront?sslmode=require")

# Update DATABASES setting with parsed database URL
DATABASES = {
    'default': db_from_env
}
#