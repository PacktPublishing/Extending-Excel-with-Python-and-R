import pandas as pd
import openpyxl
from openpyxl.utils.dataframe import dataframe_to_rows
from openpyxl.formatting.rule import ColorScaleRule

# Sample data for the heatmap
data = {
    'Category': ['A', 'B', 'C', 'D'],
    'Jan': [10, 20, 30, 40],
    'Feb': [15, 25, 35, 45],
    'Mar': [12, 22, 32, 42],
    'Apr': [18, 28, 38, 48]
}

# Convert data to a pandas DataFrame
df = pd.DataFrame(data)

# Write the DataFrame to a worksheet
df.to_excel("heatmap_with_conditional_formatting.xlsx", index=False)

# Load the workbook
wb = openpyxl.load_workbook('heatmap_with_conditional_formatting.xlsx')
ws = wb.active

# Define the range for conditional formatting (excluding the 'Category' column)
data_range = f'B2:E{len(df) + 1}'  # Adjust the range based on the DataFrame size

# Apply color scale conditional formatting to the range
color_scale_rule = ColorScaleRule(start_type='min', start_color='FFFFFF', end_type='max', end_color='FF0000')
ws.conditional_formatting.add(data_range, color_scale_rule)

# Save the workbook
wb.save('heatmap_with_conditional_formatting.xlsx')
