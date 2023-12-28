# Import necessary libraries
import pandas as pd
import numpy as np
import statsmodels.api as sm
from scipy.stats import norm
import matplotlib.pyplot as plt

# Load the time series data (replace with your data)
time_series_data = pd.read_excel('time_series_data.xlsx')['Value']

# Perform the Augmented Dickey-Fuller test to check for stationarity
result = sm.tsa.adfuller(time_series_data, autolag='AIC')

# If the p-value is greater than a threshold (e.g., 0.05), perform differencing to make the data stationary
if result[1] > 0.05:
    differenced_data = np.diff(time_series_data, n=1)
else:
    differenced_data = time_series_data

# Build an ARIMA model
order = (1, 1, 1)  # Replace with appropriate values based on ACF and PACF analysis
model = sm.tsa.ARIMA(differenced_data, order=order)

# Fit the ARIMA model
model_fit = model.fit()

# Make forecasts
forecast_steps = 50  # Adjust the number of forecast steps as needed
forecast = model_fit.forecast(steps=forecast_steps)

# If the p-value is greater than a threshold (e.g., 0.05), perform differencing to make the data stationary
if result[1] > 0.05:
    # The model was trained on the differenced data so the forecasts have to be added to the last data point
    cumsum_forecasts = np.cumsum(forecast)

    # Add this cumulative sum to the last observed value in your raw data
    real_forecasts = cumsum_forecasts + time_series_data[len(time_series_data)-1]

else:
    real_forecasts = forecast

# Retrieve ARIMA model parameters
params = model_fit.params
p, d, q = order
resid = model_fit.resid

# Compute the standard errors
stderr = np.std(resid)

# Calculate the confidence intervals
z_score = norm.ppf(0.975)  # For a 95% confidence interval
conf_int = np.column_stack((real_forecasts - z_score * stderr, real_forecasts + z_score * stderr))

# Separate the forecasts into point forecasts and confidence intervals
point_forecasts = real_forecasts  # The point forecasts
forecast_stderr = stderr  # The standard errors of the forecasts
lower_bound = conf_int[:, 0]  # Lower confidence interval bounds
upper_bound = conf_int[:, 1]  # Upper confidence interval bounds

# Visualize the original time series and forecasts
plt.figure(figsize=(12, 6))
plt.plot(time_series_data, label='Original Time Series', color='blue')
plt.plot(range(len(time_series_data), len(time_series_data) + forecast_steps), real_forecasts, label='Forecast', color='red')
plt.fill_between(range(len(time_series_data), len(time_series_data) + forecast_steps), conf_int[:, 0], conf_int[:, 1], color='pink', alpha=0.5)
plt.xlabel('Time Steps')
plt.ylabel('Value')
plt.title('ARIMA Time Series Forecast')
plt.legend()
plt.show()
