# Load the data
import pandas as pd

# Read the data back into pandas
df = pd.read_excel('time_series_data.xlsx')

# Augmented Dickey-Fuller Test

from statsmodels.tsa.stattools import adfuller

adf_result = adfuller(df['Value'])
print("\nAugmented Dickey-Fuller Test:")
print(f"ADF Statistic: {adf_result[0]}")
print(f"P-value: {adf_result[1]}")
print("Null Hypothesis (H0): Data is non-stationary")
print("Alternative Hypothesis (H1): Data is stationary")

if adf_result[1] <= 0.05:
    print("Result: Reject the null hypothesis. Data is stationary.")
else:
    print("Result: Fail to reject the null hypothesis. Data is non-stationary.")

# Print ADF test results
print("Test Statistic:", adf_result[0])
print("p-value:", adf_result[1])
print("Lags Used:", adf_result[2])
print("Number of Observations Used for the ADF Regression:", adf_result[3])
print("Critical Values:")
for key, value in adf_result[4].items():
    print(f"  {key}: {value}")
print("Maximized Information Criterion (IC):", adf_result[5])

# Time Series Decomposition

from statsmodels.tsa.seasonal import seasonal_decompose
import matplotlib.pyplot as plt

decomposition = seasonal_decompose(df['Value'], model='additive', period=365)
trend = decomposition.trend
seasonal = decomposition.seasonal
residual = decomposition.resid

# Plot the decomposition components
plt.figure(figsize=(12, 8))
plt.subplot(411)
plt.plot(df['Date'], df['Value'], label='Original')
plt.legend(loc='best')
plt.subplot(412)
plt.plot(df['Date'], trend, label='Trend')
plt.legend(loc='best')
plt.subplot(413)
plt.plot(df['Date'], seasonal, label='Seasonal')
plt.legend(loc='best')
plt.subplot(414)
plt.plot(df['Date'], residual, label='Residual')
plt.legend(loc='best')
plt.suptitle("Time Series Decomposition")
plt.show()
