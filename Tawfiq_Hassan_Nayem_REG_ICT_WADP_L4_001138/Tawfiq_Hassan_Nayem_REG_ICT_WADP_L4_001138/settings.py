

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/6.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-%n05#=7g)3!1grx6z*th(&ald7nve*fz=fd8^7n2g420c0c4$z'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'job-portal-fnj4.onrender.com']

AUTH_USER_MODEL = 'jobApp.User'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'jobApp',
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

ROOT_URLCONF = 'Tawfiq_Hassan_Nayem_REG_ICT_WADP_L4_001138.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Tawfiq_Hassan_Nayem_REG_ICT_WADP_L4_001138.wsgi.application'


# Database
# https://docs.djangoproject.com/en/6.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/6.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/6.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True



STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'


MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'






























































'''


Job 01: Develop a job Portal

Develop a job portal using Django. In this project you have to incorporate multiple recruiters and multiple job seekers from different domains on one platform. A single recruiter can post multiple job openings using his/her account. A single job seeker can apply for multiple openings based on his skills. Both recruiters and job seekers are able to manage their account using a profile manager.

Job Specification Information:

Create a project named Name_ID_JobPortal.

Develop a registration page using the following fields
(Username, Display name, Email, Password, Confirm Password, User type)

Develop a login page using the following fields
(Username and Password)

Develop a profile creation page based on user type
a. Recruiters (Company information)
b. Jobseekers (Skills set and resume upload option)

Develop a job posting page for recruiters
(Title, Number of openings, Category, Job description, Skills set)

Develop a job applying page for jobseeker (Search)

Develop a skill matching page for both recruiters and jobseeker
(Dashboard for skill matched job)

Job Specification Information:

Create a Django Project. (Naming Convention: Name_ID_Project)

Create a Database.

Store the Database.

If you want, I can also:

Convert this into exam-ready format

Help you design the Django models

Or explain each requirement step by step


'''