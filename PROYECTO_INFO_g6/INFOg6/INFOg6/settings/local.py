from .base import*

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'sql_server.pyodbc',
        'NAME':'Grupo6DB',
        'Trusted_Connection':'yes',
        'HOST' : 'localhost\SQLEXPRESS',
        'OPTIONS':{
        	'driver':'SQL Server Native Client 11.0',
        }
    },
}
'''
'default': {
        'ENGINE': 'sql_server.pyodbc',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
        'OPTIONS': {
            'driver': 'SQL Server Native Client 11.0',
            }
    },
  '''