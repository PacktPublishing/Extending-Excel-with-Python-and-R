# Import the required modules from the `win32com.client` package:
import win32com.client as win32

# Create a new instance of Excel and make it visible:
excel = win32.Dispatch('Excel.Application')
excel.Visible = True

# Create a new workbook or open an existing one:
workbook = excel.Workbooks.Add()  # Create a new workbook
# Or to open an existing workbook:
# workbook = excel.Workbooks.Open('path/to/your/workbook.xlsx')

# Get the reference to the sheet where you want to create the Pivot Table:
sheet = workbook.ActiveSheet  # Get the active sheet
# Or specify the sheet by its name:
# sheet = workbook.Sheets('Sheet1')

# Populate the data into the sheet (optional, if you have data to analyze):
# Sample data
data = [
    ['Product', 'Category', 'Sales'],
    ['Product A', 'Category 1', 100],
    ['Product B', 'Category 2', 200],
    ['Product C', 'Category 1', 150],
    ['Product D', 'Category 2', 50],
    # Add more data rows here...
]

# Write the data to the sheet
for row_index, row in enumerate(data, start=1):
    for col_index, value in enumerate(row, start=1):
        sheet.Cells(row_index, col_index).Value = value

# Add a new worksheet to the workbook to hold the Pivot Table:
pivot_table_sheet = workbook.Worksheets.Add()
pivot_table_sheet.Name = 'Pivot Table'

# Create a Pivot Cache using the data range:
pivot_cache = workbook.PivotCaches().Create(SourceType=1, SourceData=sheet.UsedRange)

# Create the Pivot Table on the new sheet using the Pivot Cache:
pivot_table = pivot_cache.CreatePivotTable(TableDestination=pivot_table_sheet.Cells(3, 1), TableName='MyPivotTable')

# Add fields to the Pivot Table, specifying their orientation (rows, columns, data, etc.):
pivot_table.PivotFields('Product').Orientation = 1 # row field
pivot_table.PivotFields('Category').Orientation = 2 # column field
pivot_table.PivotFields('Sales').Orientation = 4 # data field

# Control row and column grandtotals
pivot_table.ColumnGrand = True
pivot_table.RowGrand = True

# Decide which fields have Subtotals
pivot_table.PivotFields('Sales').Subtotals = [False]*12
pivot_table.PivotFields('Product').Subtotals = [False]*12
pivot_table.PivotFields('Category').Subtotals = [True]*12

# Customize labels and styles
pivot_table.ShowTableStyleRowStripes = False
pivot_table.PivotFields('Product').Caption = 'Product Name'
pivot_table.PivotFields('Sales').NumberFormat = '#,##0'
pivot_table.PivotFields('Sales').Caption = 'Total Sales'

# Save the workbook and close Excel:
workbook.SaveAs('./pivot_table.xlsx')
workbook.Close()
excel.Quit()
