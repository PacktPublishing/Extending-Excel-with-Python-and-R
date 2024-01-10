import pandas as pd
import numpy as np

# Load Excel data into a pandas DataFrame
df = pd.read_excel('dirty_data.xlsx')

# Handling Missing Data

# Identify missing values
missing_values = df.isnull().sum()

# Replace missing values with the mean (for numeric columns)
df['Age'].fillna(df['Age'].mean(), inplace=True)

# Replace missing values with the mode (for categorical columns)
# df['Salary'].fillna(df['Salary'].mode()[0], inplace=True)

# Forward-fill or backward-fill missing values
# df['ColumnWithMissingValues'].fillna(method='ffill', inplace=True)

# Interpolate missing values based on trends
# df['NumericColumn'].interpolate(method='linear', inplace=True)

# Remove rows or columns with missing data
df.dropna(axis=0, inplace=True)  # Remove rows with missing data
df.dropna(axis=1, inplace=True)  # Remove columns with missing data

# Handling Duplicates

# Detect and display duplicate rows
duplicate_rows = df[df.duplicated()]
print("Duplicate Rows:")
print(duplicate_rows)

# Remove duplicate rows
df.drop_duplicates(inplace=True)

# Handling Data Type Conversion

# Check data types
print(df.dtypes)

# Convert a column to a different data type (e.g., float)
df.loc[df['Salary']=='Missing', 'Salary'] = np.NaN
df.loc[:, 'Salary'] = df['Salary'].str.replace("$", "")
df.loc[:, 'Salary'] = df['Salary'].str.replace(",", "")
df['Salary'] = df['Salary'].astype(float)

# Now that Salary is a numeric column, we can fill the missing values with mean
df['Salary'].fillna(df['Salary'].mean(), inplace=True)

# Excel-Specific Data Issues

# No code needed, ensure Excel data is cleaned (e.g., merged cells unmerged, empty cells removed) before import
