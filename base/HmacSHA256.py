import base64
import hmac
import hashlib
import json
from config import readConfig
from operation_tool import file_operation


def sh256(co):
    secretKey = 'SwYNTwt5qPABx29Atyi0'
    Authorization =  base64.b64encode(hmac.new(str.encode(secretKey), str.encode(str(co)), digestmod=hashlib.sha256).digest())
    headers = {
        "Content-Type": "application/json",
        "channel": "default",
        "X-Token": "4b5e4c5a02",
        "Authorization": Authorization.decode('utf-8')
    }

    file_operation.write_file(headers,'headers.json')
    # config_path = readConfig.ReadConfig.get_config_path('path')
    # with open(config_path + 'headers.json', "w") as f:
    #     json.dump(headers, f)
    # print("headers 写入文件完成...")

if __name__ == '__main__':
    body1 = '{"page": "1", "pageSize": "20", "app_key": "lemondream"}'
    # print(sh256(body1))
