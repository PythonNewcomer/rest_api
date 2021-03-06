import configparser

class ConfigReader(object):
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('config.ini')

    def get_database_config(self):
        host = self.config['DB']['HOST']
        dbname = self.config['DB']['DATABASE']
        user = self.config['DB']['USER']
        password = self.config['DB']['PASSWORD']
        return host, dbname, user, password