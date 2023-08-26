import pandas as pd
import openpyxl
from openpyxl.formatting.rule import ColorScaleRule, CellIsRule, FormulaRule

# Create some sample data
data = {'Name': ['John', 'Alice', 'Michael', 'Emily'],
        'Age': [25, 30, 22, 28],
        'City': ['New York', 'London', 'Paris', 'Sydney'],
        'Sales': [1000, 800, 1200, 900]}

df = pd.DataFrame(data)

# Write the DataFrame to a worksheet
df.to_excel("conditional_formatting.xlsx", index=False)

# Load the workbook
wb = openpyxl.load_workbook('conditional_formatting.xlsx')
ws = wb.active

# Define conditional formatting rules
red_text_rule = CellIsRule(operator="lessThan", formula=["1000"], stopIfTrue=True, font=openpyxl.styles.Font(color="FF0000"))
ws.conditional_formatting.add(f"D2:D{len(df)+1}", red_text_rule)

# Define the condition for the green fill color scale
min_sales = min(df['Age'])
max_sales = max(df['Age'])

green_fill_rule = ColorScaleRule(
    start_type='num', start_value=min_sales, start_color='0000FF00',
    end_type='num', end_value=max_sales, end_color='00FFFF00')

ws.conditional_formatting.add(f"B2:B{len(df)+1}", green_fill_rule)

# Save the Excel workbook
wb.save('conditional_formatting.xlsx')
