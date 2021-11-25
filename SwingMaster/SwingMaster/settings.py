"""
Django settings for SwingMaster project.

Generated by 'django-admin startproject' using Django 3.2.8.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
<<<<<<< HEAD
import os
=======
>>>>>>> origin/cjh_analysispage

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

<<<<<<< HEAD
=======

>>>>>>> origin/cjh_analysispage
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
<<<<<<< HEAD
SECRET_KEY = 'django-insecure-=u8v^w11v3j9)n$(rouw2l6_t6oe-(a2c^b4@(s3_7$idje&ku'
=======
SECRET_KEY = 'django-insecure--5gnu79s9dlt5=pzwo&@3_jwf84ru6d8nnpz*)=1f&dn8quhts'
>>>>>>> origin/cjh_analysispage

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

<<<<<<< HEAD
ALLOWED_HOSTS = ["*"]
=======
ALLOWED_HOSTS = ['*']

>>>>>>> origin/cjh_analysispage

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
<<<<<<< HEAD
    'mypage.apps.MypageConfig',
    'mainpage.apps.MainpageConfig',
    'signup.apps.SignupConfig',
    'startpage.apps.StartpageConfig',
    'EditProfile.apps.EditprofileConfig',
=======
    'analysispage.apps.AnalysispageConfig'
>>>>>>> origin/cjh_analysispage
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'SwingMaster.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
<<<<<<< HEAD
        'DIRS': [BASE_DIR / 'templates'],
=======
        'DIRS': [],
>>>>>>> origin/cjh_analysispage
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'SwingMaster.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

<<<<<<< HEAD
DATABASES = { # 이 소스가 mariadb와 연동할 수 있게 해주는 소스
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'SwingMaster',
        'USER' : 'root',
        'PASSWORD' : 'SwingMaster',
        'HOST' : '52.79.212.88',
        'PORT' : '3306'
    }
}

LOGIN_REDIRECT_URL = '../mainpage'

LOGOUT_REDIRECT_URL = '/'
=======
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

>>>>>>> origin/cjh_analysispage

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
<<<<<<< HEAD
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# STATICFILES_DIRS = [os.path.join(APPS_DIR , "static")]
# STATICFILES_FINDERS = ["django.contrib.staticfiles.finders.FileSystemFinder",
#                     "django.contrib.staticfiles.finders.AppDirectoriesFinder",]
=======
>>>>>>> origin/cjh_analysispage

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
