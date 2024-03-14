import win32com.client as win32

# Connect to Excel
excel = win32.gencache.EnsureDispatch('Excel.Application')

# Open the workbook with the pivot table
workbook = excel.Workbooks.Open('pivot_table.xlsx')  # Replace with your workbook path
worksheet = workbook.Worksheets(1)

# Access the Pivot Table
pivot_table = worksheet.PivotTables(1)  # Use the name of your pivot table

# Filter by value (need to make the field a Page field instaed of a column field)
category_field = pivot_table.PivotFields('Category')
category_field.Orientation = 3 # page field
category_field.CurrentPage = "Category 1"

# Sort Rows or Columns
name_field = pivot_table.PivotFields('Product Name')
name_field.AutoSort(1, "Product Name")

# Define the new source data range 
new_source_data_range = 'Sheet1!A1:C5'

# Update the SourceData property of the pivot table's Table object
pivot_table.ChangePivotCache(workbook.PivotCaches().Create(SourceType=1, SourceData=new_source_data_range))

# Refresh data
pivot_table.RefreshTable()

# Save and close
workbook.Save()
workbook.Close()
excel.Quit()
