import requests
import unittest
from base import HmacSHA256,file_operation
import json
from base import readConfig
from ddt import ddt, data
from assertpy import assert_that
from operation_data import get_data

@ddt
class MyTestSuite(unittest.TestCase):
	cases = []
	datas = get_data.getData().get_case_count()
	for i in range(1, datas):
		if get_data.getData().get_is_run(i):
			cases.append(i)

	def setUp(self):
		pass

	def tearDown(self):
		pass

	@data(*cases)
	def test_lemon(self, num):
		#判断是否有依赖的字段
		if get_data.getData().get_request_depend_data(num) == 'access_token':
			token = file_operation.read_file('token.json')

		body = eval(get_data.getData().get_request_parameter(num))
		Authorization = HmacSHA256.sh258(json.dumps(body))
		headers = eval(get_data.getData().get_request_headers(num))
		path = get_data.getData().get_request_url(num)
		url = readConfig.ReadConfig.get_http('baseurl') + path
		except_data = get_data.getData().get_expect_data(num)
		try:
			if get_data.getData().get_request_method(num) == 'post':
				response = requests.post(url, json=body, headers=headers, verify=False)
				if get_data.getData().get_data_from_response(num) == 'access_token':
					datas = response.json()['data']
					token = {'access_token': datas['access_token'], 'refresh_token': datas['refresh_token']}
					file_operation.write_file(token, 'token.json')

			else:
				requests.get(url, params=body, headers=headers)
			print(response.text)

		except Exception as e:
			print('出错了:', e)

		# assert_that(response.status_code).is_equal_to(200) #接口状态200
		assert_that(response.text).contains(except_data)

if __name__ == '__main__':
	unittest.main()
