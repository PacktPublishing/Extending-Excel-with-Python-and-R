import pandas as pd

# Create a DataFrame with sample data
data = {
    'Name': ['John', 'Jane', 'Mike'],
    'Age': [25, 30, 35],
    'City': ['New York', 'London', 'Sydney']
}
df = pd.DataFrame(data)

# Export the DataFrame to an Excel file
df.to_excel('data.xlsx', index=False)
