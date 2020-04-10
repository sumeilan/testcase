from openpyxl.styles import Font
import openpyxl,xlwt,xlrd
from xlutils.copy import copy
file = 'E:\\python\\testcase\\data\\wo.xlsx'

# data = xlrd.open_workbook(file1)
# book = copy(data)
# sh = book.get_sheet(0)
# sh.write(1,1,'2222')
# book.save(file1)

workbook=openpyxl.load_workbook(filename=file)
sheet=workbook.active
print(sheet)
cell=sheet['A1']
sheet.row_dimensions[2].height= 40
sheet.column_dimensions['C'].width = 30
font=Font(name='黑体',size=12,bold=False,italic=False,color='000000')
cell.font=font
workbook.save(file)
