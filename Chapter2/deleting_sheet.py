import openpyxl

# Load an existing workbook
workbook = openpyxl.load_workbook("example.xlsx")

# Delete a sheet
sheet_name = "Sheet2"
sheet = workbook[sheet_name]
workbook.remove(sheet)
