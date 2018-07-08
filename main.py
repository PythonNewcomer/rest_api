from config_reader import ConfigReader
from database_helper import DatabaseHelper

cr = ConfigReader()
host, dbname, user, password = cr.get_database_config()
db = DatabaseHelper(host, dbname, user, password)

