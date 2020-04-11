from openpyxl.styles import Font
import openpyxl
from openpyxl.styles import Alignment

def format_excel(file):
    workbook = openpyxl.load_workbook(filename=file)
    sheets = workbook.worksheets

    for sheet in sheets:
        keys = ['B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N']
        align = Alignment(horizontal='center', vertical='center', wrap_text=True)
        font = Font(name='黑体', size=10, bold=False, italic=False, color='000000')
        for key in keys:
            sheet.column_dimensions[key].width = 14

        for index in range(0, sheet.max_row):
            for cell in list(sheet.rows)[index]:
                cell.font = font
                cell.alignment = align
            index = index + 1
            sheet.row_dimensions[index].height = 40

    workbook.save(file)



