import win32com.client as win32
import os

excel_app = win32.Dispatch("Excel.Application")
path =  os.getcwd().replace('\'','\\') + '\\'

workbook = excel_app.Workbooks.Open(path+"iris_data.xlsx")
worksheet = workbook.Worksheets("Sheet1")

data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for row_index, row_data in enumerate(data, start=1):
    for col_index, value in enumerate(row_data, start=1):
        worksheet.Cells(row_index, col_index).Value = value

workbook.Close(SaveChanges=True)
excel_app.Quit()
