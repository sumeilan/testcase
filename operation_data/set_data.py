# coding:utf-8
from operation_tool.operation_excel import OperationExcel
from operation_data import data_config
import xlwt


class setData:
    def __init__(self, sheet_id=None):
        self.sheet_id = sheet_id
        self.opera_excel = OperationExcel(sheet_id=sheet_id)

    # 写入实际结果
    def set_actual_data(self, sheet_id,row, value):
        col = int(data_config.get_actual_result())
        self.opera_excel.write_value(sheet_id,row+1, col+1, value)

    #写入测试结果
    def set_pass_fail(self, sheet_id,row, value):
        col = int(data_config.get_is_pass())
        self.opera_excel.write_value(sheet_id,row+1, col+1, value)

if __name__ == '__main__':
    row = 1
    value = 'pass'
    d = setData(sheet_id=2).set_pass_fail(row, value)

