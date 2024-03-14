import pandas as pd
import random

# Create a sample DataFrame
data = {
    'Age': [random.randint(18, 60) for _ in range(100)],
    'Gender': ['Male', 'Female'] * 50,
    'Income': [random.randint(20000, 100000) for _ in range(100)],
    'Region': ['North', 'South', 'East', 'West'] * 25
}

df = pd.DataFrame(data)

# Calculate summary statistics for numerical features
numerical_summary = df.describe()

# Calculate frequency counts and percentages for categorical features
categorical_summary = df['Gender'].value_counts(normalize=True)

print("Summary Statistics for Numerical Features:")
print(numerical_summary)

print("\nFrequency Counts and Percentages for Categorical Features (Gender):")
print(categorical_summary)
