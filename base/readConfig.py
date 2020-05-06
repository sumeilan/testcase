# -*- coding: UTF-8 -*-
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

    def set_http(name,value):
        config.set('HTTP',name,value)
        config.write(open(config_path,"r+",encoding='utf-8'))

    def get_config_path(path):
        value = config.get('PATH', path)
        return value

    def get_email(self, name):
        value = config.get('EMAIL', name)
        return value

if __name__ == '__main__':
    con = ReadConfig.get_http('baseurl')
    print(con)
    set_url = ReadConfig.set_http('baseurl','http://api.lemondream.cn')
    con1 = ReadConfig.get_http('baseurl')
    print(con1)
