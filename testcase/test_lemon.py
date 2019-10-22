import requests
import unittest
from base import HmacSHA256, file_operation
import json,time
from base import readConfig
from ddt import ddt, data, unpack
from assertpy import assert_that
from operation_data import get_data

@ddt
class MyTestSuite(unittest.TestCase):
    cases_index = []
    cases_name = []
    cases_module = []
    cases_id = []
    indexs = get_data.getData().get_case_count()
    for i in range(1, indexs):
        if get_data.getData().get_is_run(i):
            cases_index.append(i)
            cases_name.append(get_data.getData().get_case_name(i))
            cases_module.append((get_data.getData().get_module(i)))
            cases_id.append(int(get_data.getData().get_case_id(i)))
    cases = list(zip(cases_index, cases_name, cases_module, cases_id))

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @unpack
    @data(*cases)
    def test_lemon(self, index, casesname, module, id):
        # 判断测试用例是否有依赖的字段
        if get_data.getData().get_request_depend_data(index) == 'timestamp':
            timestamp = int(round(time.time() * 1000))
        if get_data.getData().get_request_depend_data(index) == 'access_token':
            token = file_operation.read_file('token.json')  # 请求的body需要token

        if len(get_data.getData().get_request_parameter(index)) == 0:
            body = {'':''}
        else:
            body = eval(get_data.getData().get_request_parameter(index))

        Authorization = HmacSHA256.sh258(json.dumps(body))  # 请求头需要Authorization
        headers = eval(get_data.getData().get_request_headers(index))
        path = get_data.getData().get_request_url(index)
        url = readConfig.ReadConfig.get_http('baseurl') + path
        except_data = get_data.getData().get_expect_data(index)
        try:
            if get_data.getData().get_request_method(index) == 'post':
                response = requests.post(url, json=body, headers=headers, verify=False)
                if get_data.getData().get_data_from_response(index) == 'access_token':
                    datas = response.json()['data']
                    token = {'access_token': datas['access_token'], 'refresh_token': datas['refresh_token']}
                    file_operation.write_file(token, 'token.json')

            else:
                requests.get(url, params=body, headers=headers)
            print(response.text)

        except Exception as e:
            print('出错了:', e)

        # assert_that(response.status_code).is_equal_to(200) #接口状态200
        for i in range(len(except_data)):
            assert_that(response.text).contains(except_data[i])


if __name__ == '__main__':
    unittest.main()
