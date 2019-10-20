import base64
import hmac,json
import hashlib
from base import file_operation
from operation_data import get_data

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

def sh258(co):
	secretKey = 'SwYNTwt5qPABx29Atyi0'
	Authorization = base64.b64encode(
		hmac.new(str.encode(secretKey), str.encode(str(co)), digestmod=hashlib.sha256).digest())
	return Authorization.decode('utf-8')

if __name__ == '__main__':
	body = get_data.getData().get_request_parameter(1)
	print('body=',body)
	A = sh256(json.dumps(eval(body)))
	print(A)

