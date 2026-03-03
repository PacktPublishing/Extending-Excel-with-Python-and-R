import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import ppscore as pps

# Generate test data with three variables
np.random.seed(0)
data = {
    'Feature1': np.random.randn(100),
    'Feature2': np.random.randn(100) * 2,
}

# Create a linear Target variable based on Feature1 and a non-linear function of Feature2
data['Target'] = data['Feature1'] * 2 + np.sin(data['Feature2']) + np.random.randn(100) * 0.5

# Create a DataFrame
df = pd.DataFrame(data)

# Calculate and plot the correlation heatmap
corr_matrix = df.corr()
plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5)
plt.title('Correlation Heatmap')
plt.show()

# Calculate the Predictive Power Score (PPS)
plt.figure(figsize=(8, 6))
matrix_df = pps.matrix(df)[['x', 'y', 'ppscore']].pivot(columns='x', index='y', values='ppscore')
sns.heatmap(matrix_df, vmin=0, vmax=1, cmap="Blues", linewidths=0.5, annot=True)
plt.title("Predictive Power Score (PPS) Heatmap")
plt.show()

# Additional insights
correlation_target = df['Feature1'].corr(df['Target'])
pps_target = pps.score(df, 'Feature1', 'Target')['ppscore']

print(f'Correlation between Feature1 and Target: {correlation_target:.2f}')
print(f'Predictive Power Score (PPS) between Feature1 and Target: {pps_target:.2f}')
