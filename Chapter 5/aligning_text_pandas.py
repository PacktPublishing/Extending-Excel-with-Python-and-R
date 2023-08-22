# Pandas example for aligning text within cells
import pandas as pd

data = {'Name': ['John', 'Alice', 'Michael'],
        'Age': [25, 30, 22],
        'City': ['New York', 'London', 'Paris']}

df = pd.DataFrame(data)

# Applying text alignment
alignment_styles = {'text-align': 'center'}
styled_df = df.style.set_properties(subset=['Name', 'Age', 'City'], **alignment_styles)
styled_df.to_excel('aligned_table_pandas.xlsx', index=False)
