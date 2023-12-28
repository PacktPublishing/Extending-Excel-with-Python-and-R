# Sample Data Generation
import pandas as pd
import random
from datetime import datetime, timedelta
import win32com.client as win32
import os 
import numpy as np

data = {
    'Date': [datetime(2023, 1, 1) + timedelta(days=i) for i in range(365)],
    'Sales': [random.randint(100, 1000) for _ in range(365)]
}

df = pd.DataFrame(data)

# Create an ExcelWriter object and write the DataFrame to the Excel worksheet
df.to_excel("GroupingExample.xlsx", sheet_name='Sheet1', index=False)

# Connect to Excel
excel = win32.gencache.EnsureDispatch('Excel.Application')

# Create an Excel workbook and add a sheet
wd = os.getcwd()
workbook = excel.Workbooks.Open(os.path.join(wd, 'GroupingExample.xlsx'))  # Replace with your workbook path
worksheet = workbook.Worksheets(1)

# Add a new worksheet to the workbook to hold the Pivot Table:
pivot_table_sheet = workbook.Worksheets.Add()
pivot_table_sheet.Name = 'Pivot Table'

# Define the range of data to be used as input for the pivot table
data_range = worksheet.Range('A1:B365') 

# Create a Pivot Cache using the data range:
pivot_cache = workbook.PivotCaches().Create(SourceType=1, SourceData=data_range)

starting_row = 3

# Create the Pivot Table on the new sheet using the Pivot Cache:
pivot_table = pivot_cache.CreatePivotTable(TableDestination=pivot_table_sheet.Cells(starting_row, 1), TableName='MyPivotTable')

# Add the 'Date' field to Rows
date_field = pivot_table.PivotFields('Date')
date_field.Orientation = 1 # row field
pivot_table.PivotFields('Sales').Orientation = 4 # data field

# Add the calculated fields
calculated_field = pivot_table.CalculatedFields().Add("Total Sales", "=SUM(Sales)")

# Group by months
date_field.Subtotals = [False]*12
date_field.NumberFormat = 'MMMM YYYY'

# Sort Rows
date_field.AutoSort(1, "Date")

# count the unique values for each value of the date column in the pivot
date_values = pd.DataFrame([item.Value for item in date_field.PivotItems()], columns = ['date'])
unique_values = pd.DataFrame(np.transpose(np.unique(date_values, return_counts=True)), columns=['date', 'count'])
date_values_count = date_values.merge(unique_values).drop_duplicates()

# Group by months
# Set the GroupOn property
date_range = pivot_table_sheet.Range(f"A4:A{starting_row + date_values_count['count'].iloc[0]}")
date_range.Group()

# You can use the above method to group the other months as well if you want to
# Note: the pivot is now changed, the second group starts at row starting_row + 2, instead of starting_row + 32

# change the formatting of the grouped column to show only month and year and change back the original date column to show the full date
pivot_table.PivotFields('Date2').NumberFormat = 'MMMM YYYY'
date_field.NumberFormat = 'DD MMMM YYYY'

# hide the details of the grouped values
for item in pivot_table.PivotFields('Date2').PivotItems():
    item.ShowDetail = False

# Refresh data
pivot_table.RefreshTable()

#pivot_table.PivotFields('Date2').Orientation = 2

# Save and close
workbook.Save()
workbook.Close()
excel.Quit()
