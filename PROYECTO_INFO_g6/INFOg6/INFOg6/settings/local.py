from .base import *

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'sql_server.pyodbc',
        'NAME':'Grupo6DB',
        'HOST':'localhost',
        'USER':'SA',
        'PASSWORD':'c@rl0spec3',
        'OPTIONS':{
        	'driver':'ODBC Driver 17 for SQL Server',
        }
    },
}

