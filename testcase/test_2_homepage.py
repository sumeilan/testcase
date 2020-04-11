import requests
import unittest
from base import HmacSHA256, file_operation
import json
from base import readConfig, get_id
from ddt import ddt, data, unpack
from assertpy import assert_that
from operation_data import get_data, set_data

@ddt
class MyTestSuite(unittest.TestCase):
    globals()['sheet_id'] = 2
    cases_index = []
    cases_name = []
    cases_module = []
    cases_id = []
    datas = get_data.getData(globals()['sheet_id'])  # 首页模块
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
        pass

    def tearDown(self):
        pass

    @unpack
    @data(*cases)
    def test_homepage(self, index, casesname, module, id):
        # 判断测试用例是否有依赖的字段
        if MyTestSuite.datas.get_request_depend_data(index) == 'access_token':
            token = file_operation.read_file('token.json')  # 请求的body需要token

        if len(MyTestSuite.datas.get_request_parameter(index)) == 0:
            body = {'': ''}
        else:
            body = eval(MyTestSuite.datas.get_request_parameter(index))

        Authorization = HmacSHA256.sh258(json.dumps(body))  # 请求头需要Authorization
        biData = str(file_operation.read_file('biD.json'))
        headers = eval(MyTestSuite.datas.get_request_headers(index))
        path = MyTestSuite.datas.get_request_url(index)
        url = readConfig.ReadConfig.get_http('baseurl') + path
        except_data = MyTestSuite.datas.get_expect_data(index)

        try:
            if MyTestSuite.datas.get_request_method(index) == 'post':
                response = requests.post(url, json=body, headers=headers, verify=False)
                datas = response.json()['data']['list']
                MyTestSuite.result.set_actual_data(globals()['sheet_id'],index,str(response.json()))  # 将实际结果写入excel
                # print(json.dumps(response.json(), ensure_ascii=False, sort_keys=True, indent=2))  #格式化显示返回的数据
                if MyTestSuite.datas.get_data_from_response(index) == 'obj_id':    #需要保存的返回字段
                    if get_id.get_external_picture_id(datas):
                        external_picture_id = {'external_picture_id': get_id.get_external_picture_id(datas)}
                        file_operation.write_file(external_picture_id, 'external_picture_id.json')
            else:
                requests.get(url, params=body, headers=headers)

        except Exception as e:
            print('执行报错啦:', e)

        assert_that(response.status_code).is_equal_to(200)  # 接口状态200
        for i in range(len(except_data)):
            if assert_that(response.text).contains(except_data[i]).is_true():
                MyTestSuite.result.set_pass_fail(globals()['sheet_id'],index, 'pass')  # 写入测试结果

if __name__ == '__main__':
    unittest.main()
