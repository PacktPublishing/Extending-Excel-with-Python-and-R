import win32com.client as win32

# Connect to Excel
excel = win32.gencache.EnsureDispatch('Excel.Application')

# Open the workbook with the pivot table
workbook = excel.Workbooks.Open('PivotTableExample.xlsx')  # Replace with your workbook path
worksheet = workbook.Worksheets(1)

pivot_table = worksheet.PivotTables('MyPivotTable')  # Use the name of your pivot table

# Filter by value (need to make the field a Page field instaed of a column field)
category_field = pivot_table.PivotFields('Category')
category_field.Orientation = 3 # page field
category_field.CurrentPage = "Electronics"

# Sort Rows or Columns
name_field = pivot_table.PivotFields('Name')
name_field.AutoSort(1, "Name")

# Define the new source data range 
new_source_data_range = 'Sheet1!A1:C2'

# Update the SourceData property of the pivot table's Table object
pivot_table.TableRange2(workbook.Sheets('Sheet1').Range(new_source_data_range))

# Refresh data
pivot_table.RefreshTable()

# Save and close
workbook.Save()
workbook.Close()
excel.Quit()
