import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create a time index
date_rng = pd.date_range(start='2022-01-01', end='2023-12-31', freq='D')

# Create a trend component
trend = 0.05 * np.arange(len(date_rng))

# Create a seasonal component (cyclicality)
seasonal = 2.5 * np.sin(2 * np.pi * np.arange(len(date_rng)) / 365)

# Add some random noise
noise = np.random.normal(0, 0.5, len(date_rng))

# Combine all components to create the time series
time_series = trend + seasonal + noise

# Create a DataFrame
df = pd.DataFrame({'Date': date_rng, 'Value': time_series})

# Save the data to an Excel file
df.to_excel('time_series_data.xlsx', index=False)

# Read the data back into pandas
loaded_df = pd.read_excel('time_series_data.xlsx')

# Display the first few rows
print(loaded_df.head())
