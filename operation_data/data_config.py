# coding:utf-8
class global_var:
    case_id = '0'
    module = '1'
    case_name = '2'
    url = '3'
    request_method = '4'
    request_headers = '5'
    request_parameter = '6'
    data_from_response = '7'
    request_depend_data ='8'
    expect_result = '9'
    actual_result = '10'
    is_run = '11'
    is_pass = '12'

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

#获取请求头
def get_request_headers():
    return global_var.request_headers

#获取请求参数
def get_request_parameter():
    return global_var.request_parameter

#获取预期结果
def get_expect_result():
    return global_var.expect_result

#获取实际结果
def get_actual_result():
    return global_var.actual_result

#需要从返回结果中保存的字段
def get_data_from_response():
    return global_var.data_from_response

#获取数据依赖的字段
def get_request_depend_data():
    return global_var.request_depend_data

#获取是否执行
def get_is_run():
    return global_var.is_run

#获取测试结果
def get_is_pass():
    return global_var.is_pass








