import win32com.client as win32
import os

excel_app = win32.Dispatch("Excel.Application")
path =  os.getcwd().replace('\'','\\') + '\\'

workbook = excel_app.Workbooks.Open(path+"iris_data.xlsx")
worksheet = workbook.Worksheets("Sheet1")

# Access multiple cells using Range notation
range_of_cells = worksheet.Range('A1:C3')

# Read the values from the range of cells
values = range_of_cells.Value

workbook.Close(SaveChanges=False)
excel_app.Quit()

print(values)
