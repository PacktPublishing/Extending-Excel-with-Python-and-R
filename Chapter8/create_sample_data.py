import pandas as pd
import numpy as np

# Create a DataFrame with missing data, duplicates, and mixed data types
data = {
    'ID': [1, 2, 3, 4, 5, 6],
    'Name': ['Alice', 'Bob', 'Charlie', 'Alice', 'Eva', 'Eva'],
    'Age': [25, np.nan, 30, 28, 22, 23],
    'Salary': ['$50,000', '$60,000', 'Missing', '$65,000', '$55,000', '$75,000']
}

df = pd.DataFrame(data)

# Introduce some missing data
df.loc[1, 'Age'] = np.nan
df.loc[3, 'Salary'] = np.nan

# Introduce duplicates
df = pd.concat([df, df.iloc[1:3]], ignore_index=True)

# Save the sample data in the current working directory
df.to_excel('dirty_data.xlsx')
