from pathlib import Path
from os import path,getenv
from dotenv import load_dotenv


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# initial around enviroments
load_dotenv()

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = str(getenv('SECRET_KEY'))

if not(SECRET_KEY):
    exit(1)
    
    
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


#corsheader

#post csrf
#CSRF_TRUSTED_ORIGINS = [""]

#root config Urls
ROOT_URLCONF = 'core.urls'

#wsgi config application
WSGI_APPLICATION = 'core.wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'es-co'

TIME_ZONE = 'America/Lima'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)

STATIC_URL = 'static/'
STATICFILES_DIRS = path.join(BASE_DIR,'static'),
STATIC_ROOT = path.join(BASE_DIR,'static','static')

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'