"""
Django settings for core project.
"""

import os
from pathlib import Path
from azure.identity import ManagedIdentityCredential, ClientSecretCredential
from storages.backends.azure_storage import AzureStorage

# Build paths
BASE_DIR = Path(__file__).resolve().parent.parent

# -------------------------------------------------------------------
# General
# -------------------------------------------------------------------

SECRET_KEY = os.getenv(
    "SECRET",
    "dev-secret-key-unsafe"  # fallback for local only
)

DEBUG = True

hostname = os.environ.get("WEBSITE_HOSTNAME")
if hostname:
    ALLOWED_HOSTS = [hostname]
    CSRF_TRUSTED_ORIGINS = [f"https://{hostname}"]
else:
    ALLOWED_HOSTS = ["localhost", "127.0.0.1"]
    CSRF_TRUSTED_ORIGINS = ["http://localhost", "http://127.0.0.1"]

# -------------------------------------------------------------------
# Applications
# -------------------------------------------------------------------

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "newapp",
    "storages",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "core.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "core.wsgi.application"

# -------------------------------------------------------------------
# Database
# -------------------------------------------------------------------

if DEBUG:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.mysql",
            "NAME": os.getenv("AZURE_MYSQL_NAME"),
            "USER": os.getenv("AZURE_MYSQL_USER"),
            "PASSWORD": os.getenv("AZURE_MYSQL_PASSWORD"),
            "HOST": os.getenv("AZURE_MYSQL_HOST"),
            "PORT": "3306",
            "OPTIONS": {
                "driver": "ODBC Driver 18 for SQL Server",
                "Encrypt": "yes",
                "TrustServerCertificate": "no",
                "Connection Timeout": 60,
            },
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.mysql",
            "NAME": os.getenv("AZURE_MYSQL_NAME"),
            "USER": os.getenv("AZURE_MYSQL_USER"),
            "PASSWORD": os.getenv("AZURE_MYSQL_PASSWORD"),
            "HOST": os.getenv("AZURE_MYSQL_HOST"),
            "PORT": "3306",
            "OPTIONS": {
                "driver": "ODBC Driver 18 for SQL Server",
                "Encrypt": "yes",
                "TrustServerCertificate": "no",
                "Connection Timeout": 60,
            },
        }
    }

# -------------------------------------------------------------------
# Static & Media
# -------------------------------------------------------------------

if DEBUG:
    STATIC_URL = "/static/"
    STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
    STATIC_ROOT = BASE_DIR / "staticfiles"
else:
    STATIC_URL = "/static/"
    STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
    STATIC_ROOT = BASE_DIR / "staticfiles"

    class AzureMediaStorage(AzureStorage):
        account_name = "mediafilesstorage8900"
        account_key = os.environ.get("AZURE_ACCOUNT_KEY")
        azure_container = "media"
        expiration_secs = None

    DEFAULT_FILE_STORAGE = "core.settings.AzureMediaStorage"
    MEDIA_URL = f"https://mediafilesstorage8900.blob.core.windows.net/media/"

# -------------------------------------------------------------------
# Auth & Security
# -------------------------------------------------------------------

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
