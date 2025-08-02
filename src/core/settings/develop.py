from core.settings.base import *  # noqa

DEBUG = True

ALLOWED_HOSTS = ["localhost"]
CSRF_TRUSTED_ORIGINS = ["http://localhost:8000"]

INSTALLED_APPS += ["debug_toolbar"]
MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]
INTERNAL_IPS = ["127.0.0.1"]
