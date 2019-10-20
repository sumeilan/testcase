import os
import configparser

# path = os.path.split(os.path.realpath(__file__))[0]
path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
config_path = os.path.join(path, 'config\config.ini')
config = configparser.ConfigParser()
config.read(config_path, encoding='utf-8')

class ReadConfig():
    def get_http(name):
        value = config.get('HTTP', name)
        return value

    def get_config_path(path):
        value = config.get('PATH', path)
        return value

    def get_email(self, name):
        value = config.get('EMAIL', name)
        return value

if __name__ == '__main__':
    pass
    # print(config_path)
    # con = ReadConfig.get_config_path('path')
    # print(con)
