#coding:utf-8
from operation_tool.operation_excel import OperationExcel
from operation_data import data_config

class getData:
    def __init__(self):
        self.opera_excel = OperationExcel()

    #去获取excel行数，即case个数
    def get_case_count(self):
        return self.opera_excel.get_lines()

    # 获取是否执行
    def get_is_run(self, row):
        pass

    # 获取请求方式
    def get_request_method(self, row):
        pass

    # 获取url
    def get_request_url(self, row):
        pass

    # 获取请求参数
    def get_request_data(self, row):
        pass

if __name__ == '__main__':
    datas = getData()

