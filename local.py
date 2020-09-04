from .common import *

MEDIA_URL = "http://127.0.0.1/media/"
STATIC_URL = "http://127.0.0.1/static/"
SITES["front"]["scheme"] = "http"
SITES["front"]["domain"] = "127.0.0.1"

DATABASES["default"]["NAME"] = "platform"
DATABASES["default"]["USER"] = "platform"
DATABASES["default"]["PASSWORD"] = "platform!2020"
DATABASES["default"]["HOST"] = "db"
# DATABASES["default"]["PORT"] = 

SECRET_KEY = "shsnhsdjlajeuncsouer" # "theveryultratopsecretkey"

DEBUG = False
PUBLIC_REGISTER_ENABLED = True

DEFAULT_FROM_EMAIL = "no-reply@example.com"
SERVER_EMAIL = DEFAULT_FROM_EMAIL

CELERY_ENABLED = True

EVENTS_PUSH_BACKEND = "taiga.events.backends.rabbitmq.EventsPushBackend"
EVENTS_PUSH_BACKEND_OPTIONS = {"url": "amqp://platform:platform!2020@rabbit"}

# Uncomment and populate with proper connection parameters
# to enable email sending. `EMAIL_HOST_USER` should end by @<domain>.<tld>
#EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
#EMAIL_USE_TLS = False
#EMAIL_HOST = "localhost"
#EMAIL_HOST_USER = ""
#EMAIL_HOST_PASSWORD = ""
#EMAIL_PORT = 25

# Uncomment and populate with proper connection parameters
# to enable GitHub login/sign-in.
#GITHUB_API_CLIENT_ID = "yourgithubclientid"
#GITHUB_API_CLIENT_SECRET = "yourgithubclientsecret"