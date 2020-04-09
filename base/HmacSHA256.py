import base64
import hmac, json
import hashlib
from base import file_operation
from operation_data import get_data


def sh256(co):
    secretKey = 'SwYNTwt5qPABx29Atyi0'
    Authorization = base64.b64encode(
        hmac.new(str.encode(secretKey), str.encode(str(co)), digestmod=hashlib.sha256).digest())
    print(Authorization)
    headers = {
        "Content-Type": "application/json",
        "channel": "default",
        "X-Token": "4b5e4c5a02",
        "Authorization": Authorization.decode('utf-8')
    }

    file_operation.write_file(headers, 'headers.json')


def sh258(co):
    secretKey = 'SwYNTwt5qPABx29Atyi0'
    Authorization = base64.b64encode(
        hmac.new(str.encode(secretKey), str.encode(str(co)), digestmod=hashlib.sha256).digest())
    return Authorization.decode('utf-8')


if __name__ == '__main__':
    body = {'page': '1', 'pageSize': '20', 'app_key': 'lemondream'}
    body1 = {'': ''}
    print(type(body1))
    A = sh256(json.dumps(body1))
    print(A)
