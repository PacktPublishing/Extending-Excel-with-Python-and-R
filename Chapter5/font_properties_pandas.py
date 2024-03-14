# Pandas example for setting font properties
import pandas as pd

data = {'Name': ['John', 'Alice', 'Michael'],
        'Age': [25, 30, 22],
        'City': ['New York', 'London', 'Paris']}

df = pd.DataFrame(data)

# Define a function to apply font properties
def apply_font_properties(value):
    return 'font-weight: bold; font-size: 14px; font-style: italic; color: blue'

# Applying font properties
styled_df = df.style.applymap(apply_font_properties, subset='Name')

# Save the styled DataFrame to an Excel file
styled_df.to_excel('styled_table_pandas.xlsx', index=False)
