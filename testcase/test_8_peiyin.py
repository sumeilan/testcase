import requests, unittest
from base import result_assert
from base import readConfig, handle_datas
from ddt import ddt, data, unpack
from operation_data import get_data, set_data


@ddt
class MyTestSuite(unittest.TestCase):
    globals()['sheet_id'] = 8# app通用
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
    def test_peiyin(self, index, casesname, module, id):
        body = handle_datas.handleDatas(globals()['sheet_id']).get_request_parameter(index)
        headers = handle_datas.handleDatas(globals()['sheet_id']).get_request_headers(index, body)
        path = MyTestSuite.datas.get_request_url(index)
        url = readConfig.ReadConfig.get_http('baseurl') + path
        except_data = MyTestSuite.datas.get_expect_data(index)

        try:
            if MyTestSuite.datas.get_request_method(index) == 'post':
                response = requests.post(url, json=body, headers=headers, verify=False)
            else:
                response = requests.get(url, params=body, headers=headers)

            handle_datas.handleDatas(globals()['sheet_id']).get_data_from_response(index, response.json())  # 保存需要保存的数据
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
