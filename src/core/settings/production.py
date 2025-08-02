from core.settings.base import *  # noqa

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = []

CSRF_TRUSTED_ORIGINS = []

ADMINS = []

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "mail_admins": {
            "level": "ERROR",
            "class": "django.utils.log.AdminEmailHandler",
            "include_html": True,
        },
        "logfile": {
            "level": "INFO",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": "/logs/boilerplate.log",
            "maxBytes": 1 * 1024 * 1024,
            "backupCount": 4,
        },
    },
    "loggers": {
        "django.request": {
            "handlers": ["mail_admins"],
            "level": "ERROR",
            "propagate": True,
        },
        "django": {
            "handlers": ["logfile"],
            "level": "INFO",
            "propagate": True,
        },
    },
}
