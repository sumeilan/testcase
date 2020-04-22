#! /usr/bin/python
# coding:utf-8

from base import readConfig
import json


def read_file(filename):
    config_path = readConfig.ReadConfig.get_config_path('path') + 'data\\'
    try:
        with open(config_path + filename, 'r') as load_f:
            datas = json.load(load_f)
            # datas = load_f
    except Exception as e:
        print('报错了，检查是否空文件')
    return datas


#直接覆盖
def write_file(param, filename):
    config_path = readConfig.ReadConfig.get_config_path('path') + 'data\\'
    with open(config_path + filename, "w") as f:
        json.dump(param, f)

#在原来json下追加新内容
def zhui_write_file(param, filename):
    config_path = readConfig.ReadConfig.get_config_path('path') + 'data\\'
    data = read_file(filename)
    json_d = json.dumps(data)
    new = json.dumps({**json.loads(json_d), **param})
    with open(config_path + filename, "w") as f:
        json.dump({**json.loads(json_d), **param}, f)


if __name__ == '__main__':
    param = {'release_id': '200439'}
    t = {"refresh_token": "8ntsnb5uhdk7aftjd9qpvh3pr"}
    print(read_file('test.json'))
    zhui_write_file(t, 'test.json')
    print(read_file('test.json'))
