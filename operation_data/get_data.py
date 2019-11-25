#coding:utf-8
from operation_tool.operation_excel import OperationExcel
from operation_data import data_config
import re

class getData:
    def __init__(self,  sheet_id=None):
        self.sheet_id=sheet_id
        self.opera_excel = OperationExcel(sheet_id=sheet_id)

    #获取Excel的sheet
    def get_sheet_id(self):
        return self.get_sheet_id()

    #去获取excel行数，即case个数
    def get_case_count(self):
        return self.opera_excel.get_lines()

    # 获得用例编号
    def get_case_id(self, row):
        col = int(data_config.get_case_id())
        id = self.opera_excel.get_cell_value(row, col)
        return id

    #获得用例名
    def get_case_name(self,row):
        col = int(data_config.get_case_name())
        name = self.opera_excel.get_cell_value(row, col)
        return name

    #获取用例所属模块
    def get_module(self,row):
        col = int(data_config.get_module())
        module = self.opera_excel.get_cell_value(row, col)
        return module


    # 获取是否执行
    def get_is_run(self, row):
        flag = None
        col = int(data_config.get_is_run())
        run_model = self.opera_excel.get_cell_value(row,col)
        if run_model == 'yes':
            flag = True
        else:
            flag = False
        return flag

    # 获取请求方式
    def get_request_method(self, row):
        col = int(data_config.get_request_method())
        request_method = self.opera_excel.get_cell_value(row,col)
        return request_method

    # 获取url
    def get_request_url(self, row):
        col = int(data_config.get_url())
        url = self.opera_excel.get_cell_value(row,col)
        return url

    # 获取请求头
    def get_request_headers(self, row):
        col = int(data_config.get_request_headers())
        headers = self.opera_excel.get_cell_value(row, col)
        return headers

    # 获取请求参数
    def get_request_parameter(self, row):
        col = int(data_config.get_request_parameter())
        parameter = self.opera_excel.get_cell_value(row,col)
        return parameter

    #需要从返回结果中保存的字段
    def get_data_from_response(self,row):
        col = int(data_config.get_data_from_response())
        data_from_response = self.opera_excel.get_cell_value(row, col)
        if data_from_response == '':
            return None
        else:
            return data_from_response

    # 获取数据依赖的字段
    def get_request_depend_data(self,row):
        col = int(data_config.get_request_depend_data())
        depend_data = self.opera_excel.get_cell_value(row, col)
        if depend_data=='':
            return None
        else:
            return depend_data

    #获取预期结果
    def get_expect_data(self,row):
        col = int(data_config.get_expect_result())
        expect_datas = self.opera_excel.get_cell_value(row,col)
        new = re.sub(r'[\{\}]', "",expect_datas, flags=re.S)
        expect_data = new.split(',')
        return expect_data

    #通过sql 获取预期结果
    def get_expect_data_for_mysql(self,row):
        pass

if __name__ == '__main__':
    datas = getData(sheet_id=1).get_module(2)
    print(datas)


