from decouple import config


SECRET_KEY = "django-insecure-wewk=7*j*zgsu()57who-kmv!m+@u+nz(5_%^$q-g_ornvyu0&"

DEBUG = True


ALLOWED_HOSTS = ["*"]


# DATABASES = {
#     "default": {
#         "ENGINE": "djongo",
#         "NAME": "ceres",
#         "CLIENT": {
#             "host": "mongodb:27017",
#             "port": 27017,
#             "username": "root",
#             "password": "mongoadmin",
#             "authMechanism": "SCRAM-SHA-1",
#         },
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config('POSTGRES_DB'),
        'USER': config('POSTGRES_USER'),
        'PASSWORD': config('POSTGRES_PASSWORD'),
        'HOST': config('POSTGRES_HOST'),
        'PORT': config('POSTGRES_PORT'),
    }
}
