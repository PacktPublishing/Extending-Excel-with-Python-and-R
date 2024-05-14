import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import statsmodels.api as sm

# Generate sample data from a lognormal distribution
np.random.seed(0)
data = np.random.lognormal(mean=0, sigma=1, size=1000)

# Create a Pandas DataFrame
df = pd.DataFrame({'Data': data})

# Plot a histogram of the data
plt.hist(data, bins=30, color='skyblue', edgecolor='black')
plt.title('Histogram of Data')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()

# Perform the Shapiro-Wilk test for normality
shapiro_stat, shapiro_p = stats.shapiro(data)
is_normal = shapiro_p > 0.05  # Check if data is normally distributed
print(f'Shapiro-Wilk p-value: {shapiro_p}')
print(f'Is data normally distributed? {is_normal}')

# Create Q-Q plot with a Normal distribution
sm.qqplot(data, line='s', color='skyblue')
plt.title('Q-Q Plot (Normal)')
plt.xlabel('Theoretical Quantiles')
plt.ylabel('Sample Quantiles')
plt.show()

# Create Q-Q plot with a lognormal distribution
log_data = np.log(data)
sm.qqplot(log_data, line='s', color='skyblue')
plt.title('Q-Q Plot (Lognormal)')
plt.xlabel('Theoretical Quantiles')
plt.ylabel('Sample Quantiles')
plt.show()

# Calculate skewness and kurtosis
skewness = stats.skew(data)
kurtosis = stats.kurtosis(data)

print(f'Skewness: {skewness}')
print(f'Kurtosis: {kurtosis}')
