# Import necessary libraries
import pandas as pd
from prophet import Prophet
from prophet.plot import plot

# Load the time series data (replace with your data)
time_series_data = pd.read_excel('time_series_data.xlsx')

# Create a DataFrame with 'ds' and 'y' columns
df = pd.DataFrame({'ds': time_series_data['Date'], 'y': time_series_data['Value']})

# Initialize and fit the Prophet model without weekly seasonality
model = Prophet(weekly_seasonality=False)

# Add custom seasonality obtained from domain knowledge (in this case: we generated the data so)
model.add_seasonality(name='custom_season', period=365, fourier_order=5)

# Fit the customized model
model.fit(df)

# Create a dataframe for future dates
forecast_steps = 150  # Adjust the number of forecast steps as needed
future = model.make_future_dataframe(periods=forecast_steps, freq='D')

# Make predictions
forecast = model.predict(future)

# Plot the forecast
fig = model.plot(forecast)

fig.show()

# Plot components of the forecast (trend, yearly, and weekly seasonality)
fig2 = model.plot_components(forecast)

fig2.show()
