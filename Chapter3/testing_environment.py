import win32com.client as win32

excel_app = win32.Dispatch("Excel.Application")

vba_interface = excel_app.VBE

