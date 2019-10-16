# coding:utf-8
class global_var:
    # case_id
    case_id = '0'
    case_name = '1'
    module = '2'
    url = '3'
    request_method = '4'
    request_parameter = '5'
    expect_result = '6'
    actual_result = '7'
    is_pass = '8'
    is_run = '9'

#获取用例id
def get_case_id():
    return global_var.case_id

#获取用例名称
def get_case_name():
    return global_var.case_name

#获取用例模块
def get_module():
    return global_var.module

#获取url
def get_url():
    return global_var.url

#获取请求方法
def get_request_method():
    return global_var.request_method

#获取请求参数
def get_request_method():
    return global_var.request_parameter

#获取预期结果
def get_expect_result():
    return global_var.expect_result

#获取是否执行
def get_is_run():
    return global_var.is_run









