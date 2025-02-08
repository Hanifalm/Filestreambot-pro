# (c) adarsh-goel
import os
from os import getenv, environ
from dotenv import load_dotenv



load_dotenv()

class Var(object):
    MULTI_CLIENT = False
    API_ID = int(getenv('API_ID', '276561176'))
    API_HASH = str(getenv('API_HASH', '342665803240d9bf0940a96f555d21290'))
    BOT_TOKEN = str(getenv('BOT_TOKEN', '77791798110:AAHZoa_wTMF1RR_PwKr3-Sc7rIazFJuz92w'))
    name = str(getenv('name', 'filetolinkbot'))
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '4'))
    BIN_CHANNEL = int(getenv('BIN_CHANNEL', '-1002417622792'))
    PORT = int(getenv('PORT', '8080'))
    BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '94.954.170.165'))
    PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
    OWNER_ID = set(int(x) for x in os.environ.get("OWNER_ID", "5606659798").split())  
    NO_PORT = bool(getenv('NO_PORT', False))
    APP_NAME = None
    OWNER_USERNAME = str(getenv('OWNER_USERNAME', 'Hankuro6'))
    if 'DYNO' in environ:
        ON_HEROKU = True
        APP_NAME = str(getenv('APP_NAME'))
    
    else:
        ON_HEROKU = False
    FQDN = str(getenv('FQDN', '94.157.172.145:8080')) if not ON_HEROKU or getenv('FQDN', '94.150.162.165:8080') else APP_NAME+'.herokuapp.com'
    HAS_SSL=bool(getenv('HAS_SSL',False))
    if HAS_SSL:
        URL = "https://{}/".format(FQDN)
    else:
        URL = "http://{}/".format(FQDN)
    DATABASE_URL = str(getenv('DATABASE_URL', 'mongodb://localhost:27017'))
    UPDATES_CHANNEL = str(getenv('UPDATES_CHANNEL', None))
    BANNED_CHANNELS = list(set(int(x) for x in str(getenv("BANNED_CHANNELS", "-1001362659779")).split())) 
