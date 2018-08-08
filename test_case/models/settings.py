# env config
from past.builtins import execfile

ENV = 'test'

# test url test config
WEB_TEST_BASE_URL = "http://www.abc.com"

# global waiting time config
WAIT_TIME = 10

# redis config
REDIS_HOST = ''
REDIS_PORT = ''

# drive config
GECKODRIVER_PATH = 'geckodriver'

# mysql config
DB_HOST = ''
DB_PORT = ''
DB_USER = ''
DB_PASSWORD = ''

# local debugging config
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SNAPSHOT_DIRECTORY = os.path.join(BASE_DIR, 'logs')

SETTING_LOCAL_DIR = os.path.join(BASE_DIR, "settings_local.py")
if os.path.exists(SETTING_LOCAL_DIR):
    execfile(SETTING_LOCAL_DIR)