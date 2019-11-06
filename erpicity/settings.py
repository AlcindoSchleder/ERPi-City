import os
from decouple import config, Csv
from dj_database_url import parse as dburl
from configs.configs import (
    APP_DBMODE_SINGLE_DATABASE,
    APP_DBMODES,
    DEFAULT_DATABASE_MODE,
    DEFAULT_DATABASE_URL,
    DEFAULT_FROM_EMAIL,
    EMAIL_HOST,
    EMAIL_HOST_USER,
    EMAIL_HOST_PASSWORD,
    EMAIL_PORT,
    EMAIL_USE_TLS
)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', default=[], cast=Csv())

if not DEFAULT_DATABASE_MODE or DEFAULT_DATABASE_MODE not in APP_DBMODES:
    DEFAULT_DATABASE_MODE = APP_DBMODE_SINGLE_DATABASE

APP_NONE_CHOICE = (None, '*----------*')

if not DEFAULT_DATABASE_URL:
    DEFAULT_DATABASE_URL = 'sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')

DATABASES = {
    'default': config('DATABASE_URL', default=DEFAULT_DATABASE_URL, cast=dburl),
}


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # erpicity apps:
    'apps.base',
    'apps.login',
    'apps.cadastro',
    'apps.vendas',
    'apps.compras',
    'apps.fiscal',
    'apps.financeiro',
    'apps.estoque',
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # Middleware para paginas que exigem login
    'erpicity.middleware.LoginRequiredMiddleware',
    # Midleware para multi banco de dados
    'erpicity.middleware.TenantMiddleware',
]

ROOT_URLCONF = 'erpicity.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'), ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # contexto para a versao do sige
                'apps.base.context_version.erpicity_version',
                # contexto para a foto de perfil do usuario
                'apps.login.context_user.foto_usuario',
            ],
        },
    },
]

WSGI_APPLICATION = 'erpicity.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

FIXTURE_DIRS = [
    os.path.join(BASE_DIR, 'fixtures'),
]

MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
MEDIA_URL = 'media/'

SESSION_EXPIRE_AT_BROWSER_CLOSE = False

LOGIN_NOT_REQUIRED = (
    r'^/login/$',
    r'/login/esqueceu/',
    r'/login/trocarsenha/',
    r'/logout/',
)
