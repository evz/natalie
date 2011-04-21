
DEV_SERVER = True
DEBUG = True

DATABASES = {
    "default": {
        # "postgresql_psycopg2", "postgresql", "mysql", "sqlite3" or "oracle".
        "ENGINE": "postgresql_psycopg2",
        # DB name or path to database file if using sqlite3.
        "NAME": "natalie",
        # Not used with sqlite3.
        "USER": "natalie",
        # Not used with sqlite3.
        "PASSWORD": "thKQyaP1Ny1DSyCLRA",
        # Set to empty string for localhost. Not used with sqlite3.
        "HOST": "",
         # Set to empty string for default. Not used with sqlite3.
        "PORT": "",
    }
}
