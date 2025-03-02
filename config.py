import os
from datetime import datetime
from time import time, sleep

START_TIME = str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
print('\nServer is Starting - ' + START_TIME)

# Server Settings
IP    = '0.0.0.0'
PORT  = 5000
DEBUG = True

# LOG Settings
LOG_FLASK  = False
LOG_CLEAN  = True

# PATH Settings
PATH_APP  = os.path.abspath(os.path.dirname(__file__))
PATH_TMPL = os.path.join(PATH_APP, 'templates')
PATH_DB   = os.path.join(PATH_APP, 'instance')



