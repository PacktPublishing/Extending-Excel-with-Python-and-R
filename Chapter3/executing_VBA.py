import win32com.client as win32
import os

excel_app = win32.Dispatch("Excel.Application")

path =  os.getcwd().replace('\'','\\') + '\\'

workbook = excel_app.Workbooks.Open(path+"iris_data.xlsm")
excel_app.Run("examplePythonVBA")
workbook.Close(SaveChanges=True)
excel_app.Quit()
