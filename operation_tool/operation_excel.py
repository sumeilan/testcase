# coding:utf-8
import xlrd
import os
import pandas as pd
from xlutils3.copy import copy
from operation_data import merge_sheets

class OperationExcel:

    def __init__(self, file_name=None, sheet_id=0):
        if file_name:
            self.file_name = file_name
            self.sheet_id = sheet_id
        else:
            root = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
            self.file_name = root + '\data\case2.xlsx'
            self.sheet_id = sheet_id
            self.data = self.get_data()

    #根据sheet名称获得id
    def get_sheet_id(self,sheet_name):
        data = xlrd.open_workbook(self.file_name)
        i = -1
        for sheet in data.sheets():
            i =i+1
            if sheet.name == sheet_name:
                print(str(i) + sheet.name)
                self.sheet_id = i
                print('根据sheet名称获得id')
                print( self.sheet_id)
                return i

    # 获取sheets的内容
    def get_data(self):
        data = xlrd.open_workbook(self.file_name)
        tables = data.sheets()[self.sheet_id]
        return tables

    # 获取单元格的行数
    def get_lines(self):
        tables = self.data
        return tables.nrows

    # 获取某一个单元格的内容
    def get_cell_value(self, row, col):
        return self.data.cell_value(row, col)

    # 写入数据
    def write_value(self, row, col, value):
        '''
        写入excel数据
        row,col,value
        '''
        read_data = xlrd.open_workbook(self.file_name)
        write_data = copy(read_data)
        sheet_data = write_data.get_sheet(0)
        sheet_data.write(row, col, value)
        write_data.save(self.file_name)

    # 根据对应的caseid 找到对应行的内容
    def get_rows_data(self, case_id):
        row_num = self.get_row_num(case_id)
        rows_data = self.get_row_values(row_num)
        return rows_data

    # 根据对应的caseid找到对应的行号
    def get_row_num(self, case_id):
        num = 0
        clols_data = self.get_cols_data()
        for col_data in clols_data:
            if case_id in col_data:
                return num
        num = num + 1

    # 根据行号，找到该行的内容
    def get_row_values(self, row):
        tables = self.data
        row_data = tables.row_values(row)
        return row_data

    # 获取某一列的内容
    def get_cols_data(self, col_id=None):
        if col_id != None:
            cols = self.data.col_values(col_id)
        else:
            cols = self.data.col_values(0)
        return cols

if __name__ == '__main__':
    opers = OperationExcel()
    # sheet_id = opers.get_sheet_id('邀请好友注册')
    # # print(opers.get_lines())
    # print(opers.get_data())
