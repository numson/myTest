import os
from .base import *

DEBUG = False

cwd = os.getcwd()

SECRET_KEY='=b%n9y5yzx&%2o*w_pfhq!u+8js-ms_3r&4+9p_de(8@%h_11t'
ALLOWED_HOSTS=['localhost','*']
CACHES = {
    "default":{
        "BACKEND":"django.core.cache.backeds.filebased.FileBaseCache",
        "LOCATION":f"{cwd}/.cache"
    }
}

DATABASES={
    "default":{
        "ENGINE":"django.db.backends.postgresql_psycopg2",
        "NAME":"rocketman",
        "USER":"rocketman",
        "PASSWORD":'@Riskman12',
        "HOST":'localhost',
        "PORT":'',

    }
}

import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

sentry_sdk.init(
    dsn="https://482038de6673466896971e94943cfa4f@o549310.ingest.sentry.io/5671928",
    integrations=[DjangoIntegration()],

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0,

    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True
)

try:
    from .local import *
except ImportError:
    pass

