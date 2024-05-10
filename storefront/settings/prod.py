import os
from .common import *

DEBUG = False

db_from_env = dj_database_url.parse("postgres://storefront_vxz4_user:Nbstcz54DE4GzeeNH4NoP97FI2PgLleh@dpg-cov0qp021fec73c06tkg-a.oregon-postgres.render.com/storefront_vxz4")

# Update DATABASES setting with parsed database URL
DATABASES = {
    'default': db_from_env
}

ALLOWED_HOSTS = ['127.0.0.1','storefront3-wsl2.onrender.com']