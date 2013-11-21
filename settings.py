
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
          # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'database.db',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': 'localhost',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '5432',                      # Set to empty string for default. Not used with sqlite3.
    }
}
INSTALLED_APPS = ("models")


# Django will ask you for a secret kay, use generate_secret_key.py script to
# generate a string and asign it to the variable below
SECRET_KEY = ""
