# mysite/test_settings.py

from mysite.settings import *  # Use the full path for importing base settings
# Import everything from the base settings

# Use SQLite for in-memory testing to avoid the need for PostgreSQL in CI
# mysite/test_settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}


# Other adjustments to optimize for testing
DEBUG = False
ALLOWED_HOSTS = ['*']
