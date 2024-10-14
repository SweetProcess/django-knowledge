import os

DIRNAME = os.path.dirname(__file__)

DEBUG = True

DEFAULT_AUTO_FIELD = "django.db.models.AutoField"

DATABASE_ENGINE = "sqlite3"
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(DIRNAME, "example.sqlite").replace("\\", "/"),
        "USER": "",
        "PASSWORD": "",
        "HOST": "",
        "PORT": "",
    }
}

STATIC_URL = "/static/"

INTERNAL_IPS = ("127.0.0.1",)

SITE_ID = 1
SECRET_KEY = "lolz"

MIDDLEWARE = (
    "django.middleware.common.CommonMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
)

INSTALLED_APPS = (
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.admin",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.messages",
    "django_markdown",
    "knowledge",
    "django_coverage",
    "mock",
)

ROOT_URLCONF = "tests.urls"

COVERAGE_REPORT_HTML_OUTPUT_DIR = os.path.join(DIRNAME, "reports").replace("\\", "/")

TEMPLATES = [
    {
        "DIRS": (os.path.join(DIRNAME, "templates").replace("\\", "/"),),
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    },
]

LOGIN_REDIRECT_URL = "/admin/"
