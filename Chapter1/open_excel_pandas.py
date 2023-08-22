import pandas as pd

# Read the Excel file
df = pd.read_excel('iris_data.xlsx', sheet_name='setosa')

# Display the first few rows of the DataFrame
print(df.head())
