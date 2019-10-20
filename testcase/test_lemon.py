import requests
import unittest
from base import HmacSHA256,file_operation
import json,os
from base import readConfig
from ddt import ddt, data ,unpack
from assertpy import assert_that
from operation_data import get_data

@ddt
class MyTestSuite(unittest.TestCase):
	cases_id = []
	cases_name = []
	ids = get_data.getData().get_case_count()
	for i in range(1, ids):
		if get_data.getData().get_is_run(i):
			cases_id.append(i)
			cases_name.append(get_data.getData().get_case_name(i))
	cases = list(zip(cases_id, cases_name))

	def setUp(self):
		pass

	def tearDown(self):
		pass

	@unpack
	@data(*cases)
	def test_lemon(self, id,casesname):
		#判断是否有依赖的字段
		if get_data.getData().get_request_depend_data(id) == 'access_token':
			token = file_operation.read_file('token.json')

		body = eval(get_data.getData().get_request_parameter(id))
		Authorization = HmacSHA256.sh258(json.dumps(body))
		headers = eval(get_data.getData().get_request_headers(id))
		path = get_data.getData().get_request_url(id)
		url = readConfig.ReadConfig.get_http('baseurl') + path
		except_data = get_data.getData().get_expect_data(id)
		try:
			if get_data.getData().get_request_method(id) == 'post':
				response = requests.post(url, json=body, headers=headers, verify=False)
				if get_data.getData().get_data_from_response(id) == 'access_token':
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
