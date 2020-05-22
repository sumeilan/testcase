import base64
import hmac, json
import hashlib

def auth(co):
    secretKey1 = 'SwYNTwt5qPABx29Atyi0'
    secretKey2 = 'SwYNun73nlo82443Twt5qPABx29Atyi0'
    Authorization = base64.b64encode(
        hmac.new(str.encode(secretKey1), str.encode(str(co)), digestmod=hashlib.sha256).digest())
    return Authorization.decode('utf-8')

def auth2(co):
    secretKey2 = 'SwYNun73nlo82443Twt5qPABx29Atyi0'
    AuthorizationV2 = base64.b64encode(
        hmac.new(str.encode(secretKey2), str.encode(str(co)), digestmod=hashlib.sha256).digest())
    return AuthorizationV2.decode('utf-8')


if __name__ == '__main__':
    body = {'page': '1', 'pageSize': '20', 'app_key': 'lemondream'}
    body1 = {'': ''}
    print(type(body1))
    print(body)
    A = sh256(json.dumps(body))
    print(json.dumps(body))
