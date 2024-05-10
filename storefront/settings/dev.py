from .common import *
import dj_database_url

DEBUG = True

SECRET_KEY = 'django-insecure-hs6j037urx6iav+7#10%-vu4l4f5@@-1_zo)oft4g7$vf2$jmp'

# Parse the database URL
db_from_env = dj_database_url.parse("postgres://storefront_vxz4_user:Nbstcz54DE4GzeeNH4NoP97FI2PgLleh@dpg-cov0qp021fec73c06tkg-a.oregon-postgres.render.com/storefront_vxz4")

# Update DATABASES setting with parsed database URL
DATABASES = {
    'default': db_from_env
}
#