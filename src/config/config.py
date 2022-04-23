from configparser import ConfigParser
import os

from src.utils.constants.generic import ROOT_DIR


config = ConfigParser()
config_path = os.path.join(ROOT_DIR, 'config.ini')

DB_CONNECTION = ''
PORT = 0
HOST = ''
DEBUG = False

def read_config():
    global DB_CONNECTION
    global PORT
    global HOST
    global DEBUG
    
    config.read(config_path)
    print(config.get('app', 'port'))
    
    DB_CONNECTION = config.get('database', 'db_link')
    PORT = int(config.get('app', 'port')) if config.get('app', 'port') else 8000 
    HOST = str(config.get('app', 'host')) if config.get('app', 'host') else '0.0.0.0' 
    DEBUG = bool(config.get('app', 'debug')) if config.get('app', 'debug')  else True

read_config()
