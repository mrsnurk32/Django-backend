import os
from pathlib import Path
from dotenv import load_dotenv
load_dotenv()


BASE_DIR = Path(__file__).resolve().parent.parent
SQLITE_DB_CONFIG = { 
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

POSTGRESQL_DB_CONFIG = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        'NAME': os.getenv("POSTGRESS_DB", "localhost"),
        'USER': os.getenv("PG_USER", ""),
        'PASSWORD': os.getenv("PG_PASSWORD", ""),
        'HOST': os.getenv("PG_HOST", ""),
        'PORT': os.getenv("PG_PORT", ""),
    }
}

DEBUG = bool(os.getenv("DEBUG", True))

DB_CONFIG = POSTGRESQL_DB_CONFIG

if DEBUG:
    DB_CONFIG = SQLITE_DB_CONFIG