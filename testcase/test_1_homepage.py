import requests, unittest
from base import result_assert
from base import readConfig, handle_datas
from ddt import ddt, data, unpack
from operation_data import get_data, set_data


@ddt
class TestHomePage(unittest.TestCase):
    globals()['sheet_id'] = 1 # app通用
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
    def test_homepage(self, index, casesname, module, id):
        body = handle_datas.handleDatas(globals()['sheet_id']).get_request_parameter(index)
        headers = handle_datas.handleDatas(globals()['sheet_id']).get_request_headers(index, body)
        path = TestHomePage.datas.get_request_url(index)
        url = readConfig.ReadConfig.get_http('baseurl') + path
        except_data = TestHomePage.datas.get_expect_data(index)

        try:
            if TestHomePage.datas.get_request_method(index) == 'post':
                response = requests.post(url, json=body, headers=headers, verify=False)

            else:
                response = requests.get(url, params=body, headers=headers)

            print(response.text)
            handle_datas.handleDatas(globals()['sheet_id']).get_data_from_response(index, response.json())  # 保存需要保存的数据
            TestHomePage.result.set_actual_data(globals()['sheet_id'], index, str(response.json()))  # 将实际结果写入excel


        except Exception as e:
            globals()['result'] = '报错啦'
            TestHomePage.result.set_actual_data(globals()['sheet_id'], index, str(e))
            TestHomePage.result.set_pass_fail(globals()['sheet_id'], index, globals()['result'])  # 写入测试结果

        TestHomePage.result.set_pass_fail(globals()['sheet_id'], index, globals()['result'])  # 先写入测试结果为不通过
        result = result_assert.result_assert(response.text, response.status_code, except_data)  # 断言，判断接口状态和预期结果
        if result == 'pass':
            globals()['result'] = 'pass'
            TestHomePage.result.set_pass_fail(globals()['sheet_id'], index, globals()['result'])  # 更新为测试通过


if __name__ == '__main__':
    unittest.main()
