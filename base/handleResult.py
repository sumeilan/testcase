from assertpy import assert_that
import json


def out_print(url, headers, body, response):
    print("url:", url, "\n")
    print("headers:", headers, "\n")
    print("body:", body, "\n")
    print("response:", response.text)

def result_assert(response, status_code=None, expect_results=None):
    result = 'pass'
    if status_code is not None:
        assert_that(status_code).is_equal_to(200)  # 接口状态200
    if expect_results is not None:
        for i in expect_results:
            assert_that(response).contains(i)
    else:
        print('emmmmm')
    return result


if __name__ == '__main__':
    response = '{"code":0,"msg":"请求成功","uid":"1060","zone_id":-1}'
    expect_results = ['"zone_id":-1', '"uid":"10601"']
    result = result_assert(response, expect_results=expect_results)
    print(result)
