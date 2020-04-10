from openpyxl.styles import Font
import openpyxl

file = 'E:\\python\\testcase\\data\\wo.xlsx'

workbook = openpyxl.load_workbook(filename=file)
sheets = workbook.worksheets


for sheet in sheets:
    index = 0
    rows = sheet.rows
    sheet.row_dimensions[index].height = 40
    sheet.column_dimensions['F'].width = 30
    font = Font(name='黑体', size=10, bold=False, italic=False, color='000000')
    for i in range(index,len(sheets)):
        for cell in list(sheet.rows)[index]:
            cell.font = font
            print(cell)
        index = index + 1


workbook.save(file)
