# mysite/test_settings.py

from .settings import *  # Import everything from the base settings

# Use SQLite for in-memory testing to avoid the need for PostgreSQL in CI
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',  # Use in-memory SQLite database
    }
}

# Other adjustments to optimize for testing
DEBUG = False
ALLOWED_HOSTS = ['*']
