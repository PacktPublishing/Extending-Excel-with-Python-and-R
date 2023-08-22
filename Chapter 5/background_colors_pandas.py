# Pandas example for cell background colors
import pandas as pd

data = {'Name': ['John', 'Alice', 'Michael'],
        'Age': [25, 30, 22],
        'City': ['New York', 'London', 'Paris']}

df = pd.DataFrame(data)

# Create a styler object
styled_df = df.style

# Define the style for the cells
styled_df = styled_df.applymap(lambda _: 'background-color: yellow', subset=pd.IndexSlice[0, ['Name', 'Age']])

# Save the styled DataFrame to an Excel file
styled_df.to_excel('colored_table_pandas.xlsx', index=False)
