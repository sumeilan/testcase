import requests
import unittest
from base import HmacSHA256, file_operation, result_assert
import json
from base import readConfig
from ddt import ddt, data, unpack
from assertpy import assert_that
from operation_data import get_data, set_data


@ddt
class MyTestSuite(unittest.TestCase):
    globals()['sheet_id'] = 2  # 注册登录
    cases_index = []
    cases_name = []
    cases_module = []
    cases_id = []
    datas = get_data.getData(globals()['sheet_id'])
    indexs = datas.get_case_count()
    result = set_data.setData(globals()['sheet_id'])
    for i in range(1, indexs):
        if datas.get_is_run(i):
            cases_index.append(i)
            cases_name.append(datas.get_case_name(i))
            cases_module.append((datas.get_module(i)))
            cases_id.append(int(datas.get_case_id(i)))
    cases = list(zip(cases_index, cases_name, cases_module, cases_id))

    def setUp(self):
        globals()['result'] = 'fail'

    def tearDown(self):
        pass

    @unpack
    @data(*cases)
    def test_user_login(self, index, casesname, module, id):
        # 判断测试用例是否有依赖的字段
        if MyTestSuite.datas.get_request_depend_data(index) == 'access_token':
            token = file_operation.read_file('token.json')['access_token']  # 请求的body需要token
        if len(MyTestSuite.datas.get_request_parameter(index)) == 0:
            body = {'': ''}
        else:
            body = eval(MyTestSuite.datas.get_request_parameter(index))

        Authorization = HmacSHA256.sh258(json.dumps(body))  # 请求头需要Authorization
        biData = str(file_operation.read_file('biD.json'))
        XToken = file_operation.read_file('token.json')['X-Token']
        versionCode = readConfig.ReadConfig.get_http('versionCode')
        headers = eval(MyTestSuite.datas.get_request_headers(index))
        path = MyTestSuite.datas.get_request_url(index)
        url = readConfig.ReadConfig.get_http('baseurl') + path
        except_data = MyTestSuite.datas.get_expect_data(index)
        try:
            if MyTestSuite.datas.get_request_method(index) == 'post':
                response = requests.post(url, json=body, headers=headers, verify=False)
                datas = response.json()['data']
                if MyTestSuite.datas.get_data_from_response(index) == 'access_token':
                    token = {'access_token': datas['access_token'], 'refresh_token': datas['refresh_token']}
                    file_operation.zhui_write_file(token, 'token.json')
                if MyTestSuite.datas.get_data_from_response(index) == 'id':
                    uid = {'uid': datas['id']}
                    file_operation.zhui_write_file(uid, 'ids.json')
            else:
                response = requests.get(url, params=body, headers=headers)
            MyTestSuite.result.set_actual_data(globals()['sheet_id'], index, str(response.json()))  # 将实际结果写入excel

        except Exception as e:
            globals()['result'] = '报错啦'
            MyTestSuite.result.set_actual_data(globals()['sheet_id'], index, str(e))
            MyTestSuite.result.set_pass_fail(globals()['sheet_id'], index, globals()['result'])  # 写入测试结果

        MyTestSuite.result.set_pass_fail(globals()['sheet_id'], index, globals()['result'])  # 先写入测试结果为不通过
        result = result_assert.result_assert(response.text, response.status_code, except_data)  # 断言，判断接口状态和预期结果
        if result == 'pass':
            globals()['result'] = 'pass'
            MyTestSuite.result.set_pass_fail(globals()['sheet_id'], index, globals()['result'])  # 更新为测试通过


if __name__ == '__main__':
    unittest.main()
