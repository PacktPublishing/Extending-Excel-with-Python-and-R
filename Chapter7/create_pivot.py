import win32com.client as win32

# Create an Excel workbook and add a sheet
excel = win32.gencache.EnsureDispatch('Excel.Application')
workbook = excel.Workbooks.Add()
worksheet = workbook.Worksheets(1)

# Add some test data
worksheet.Cells(1, 1).Value = 'Name'
worksheet.Cells(1, 2).Value = 'Category'
worksheet.Cells(1, 3).Value = 'Sales'

worksheet.Cells(2, 1).Value = 'John'
worksheet.Cells(2, 2).Value = 'Electronics'
worksheet.Cells(2, 3).Value = 1000

worksheet.Cells(3, 1).Value = 'Alice'
worksheet.Cells(3, 2).Value = 'Clothing'
worksheet.Cells(3, 3).Value = 800

worksheet.Cells(4, 1).Value = 'John'
worksheet.Cells(4, 2).Value = 'Clothing'
worksheet.Cells(4, 3).Value = 300

# Add more data as needed

# Define the range of data to be used as input for the pivot table
data_range = worksheet.Range('A1:C4')  # Adjust the range as needed

# Add a new worksheet to the workbook to hold the Pivot Table:
pivot_table_sheet = workbook.Worksheets.Add()
pivot_table_sheet.Name = 'Pivot Table'

# Create a Pivot Cache using the data range:
pivot_cache = workbook.PivotCaches().Create(SourceType=1, SourceData=data_range)

# Create the Pivot Table on the new sheet using the Pivot Cache:
pivot_table = pivot_cache.CreatePivotTable(TableDestination=pivot_table_sheet.Cells(3, 1), TableName='MyPivotTable')

# Add the row, column and data fields
pivot_table.PivotFields('Name').Orientation = 1 # row field
pivot_table.PivotFields('Category').Orientation = 2 # column field
pivot_table.PivotFields('Sales').Orientation = 4 # data field

# Add the calculated fields
calculated_field = pivot_table.CalculatedFields().Add("Total Sales", "=SUM(Sales)")

# Refresh the PivotTable to apply changes
pivot_table.RefreshTable()

# Save the Workbook and close Excel
workbook.SaveAs('PivotTableExample.xlsx')
workbook.Close()
excel.Quit()
