import requests,unittest,json
from base import HmacSHA256, file_operation
from base import readConfig
from ddt import ddt, data, unpack
from assertpy import assert_that
from operation_data import get_data, set_data

@ddt
class MyTestSuite(unittest.TestCase):
    cases_index = []
    cases_name = []
    cases_module = []
    cases_id = []
    datas = get_data.getData(sheet_id=0)#首页模块
    indexs = datas.get_case_count()
    for i in range(1, indexs):
        if datas.get_is_run(i):
            cases_index.append(i)
            cases_name.append(datas.get_case_name(i))
            cases_module.append((datas.get_module(i)))
            cases_id.append(int(datas.get_case_id(i)))
    cases = list(zip(cases_index, cases_name, cases_module, cases_id))

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @unpack
    @data(*cases)
    def test_app_common(self, index, casesname, module, id):
        # 判断测试用例是否有依赖的字段
        if MyTestSuite.datas.get_request_depend_data(index) == 'access_token':
            token = file_operation.read_file('token.json')  # 请求的body需要token

        if len(MyTestSuite.datas.get_request_parameter(index)) == 0:
            body = {'': ''}
        else:
            body = eval(MyTestSuite.datas.get_request_parameter(index))

        Authorization = HmacSHA256.sh258(json.dumps(body))  # 请求头需要Authorization
        headers = eval(MyTestSuite.datas.get_request_headers(index))
        path = MyTestSuite.datas.get_request_url(index)
        url = readConfig.ReadConfig.get_http('baseurl') + path
        except_data = MyTestSuite.datas.get_expect_data(index)
        try:
            if MyTestSuite.datas.get_request_method(index) == 'post':
                response = requests.post(url, json=body, headers=headers, verify=False)

            else:
                requests.get(url, params=body, headers=headers)
            print(response.text)

        except Exception as e:
            print('出错了:', e)

        assert_that(response.status_code).is_equal_to(200) #接口状态200
        for i in range(len(except_data)):
            assert_that(response.text).contains(except_data[i])


if __name__ == '__main__':
    unittest.main()
