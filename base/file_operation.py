#! /usr/bin/python
# coding:utf-8

from base import readConfig
import json


def read_file(filename):
    config_path = readConfig.ReadConfig.get_config_path('path') + 'data\\'
    with open(config_path + filename, 'r') as load_f:
        datas = json.load(load_f)
    return datas


def a_write_file(param, filename):
    config_path = readConfig.ReadConfig.get_config_path('path') + 'data\\'
    with open(config_path + filename, "a") as f:
        json.dump(param, f)


def write_file(param, filename):
    config_path = readConfig.ReadConfig.get_config_path('path') + 'data\\'
    with open(config_path + filename, "w") as f:
        json.dump(param, f)


if __name__ == '__main__':
    headers = {
        "X-Token": "4b5e4c5a02",
        "Authorization": 'testttttttttttttttttttttt'
    }

    writer_headers = write_file(headers, 'headers.json')
    read_headers = read_file('headers.json')
    print(read_headers)
