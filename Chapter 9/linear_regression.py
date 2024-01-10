# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import statsmodels.api as sm 
from statsmodels.graphics.regressionplots import plot_regress_exog
from statsmodels.graphics.gofplots import qqplot

# Step 0: Generate sample data and save as Excel file
np.random.seed(0)
n_samples = 100
X = np.random.rand(n_samples, 2)  # Two features
y = 2 * X[:, 0] + 3 * X[:, 1] + np.random.randn(n_samples)  # Linear relationship with noise

# Create a pandas DataFrame
data = {'Feature1': X[:, 0], 'Feature2': X[:, 1], 'Target': y}
df = pd.DataFrame(data)

# Save the data to Excel
df.to_excel("linear_regression_input.xlsx")

# Step 1: Import Excel data into a pandas DataFrame
excel_file = "linear_regression_input.xlsx"
df = pd.read_excel(excel_file)

# Step 2: Explore the data
# Use the tools learned in the previous chapter on EDA

# Step 3: Data Preparation (if needed)
# Use the tools learned in the previous chapter on data cleaning

# Step 4: Split data into training and testing sets
X = df[['Feature1', 'Feature2']] # Independent variables
y = df['Target'] # Dependent variable

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 5: Fit the Linear Regression model
# Add a constant (intercept) to the independent variables
X_train = sm.add_constant(X_train)
X_test = sm.add_constant(X_test)

# Fit the linear model
model = sm.OLS(y_train, X_train).fit()

# Step 6: Model Evaluation
y_pred = model.predict(X_test)

# Print the model summary
print(model.summary())

# Step 7: Visualization
plt.scatter(X_test['Feature1'], y_test, color='blue', label='Actual')
plt.scatter(X_test['Feature1'], y_pred, color='red', label='Predicted')
plt.xlabel('Feature1')
plt.ylabel('Target')
plt.title('Linear Regression Prediction')
plt.legend()
plt.show()

# Set the backend to 'Agg' before generating the plots
plt.switch_backend('TkAgg')

# Residuals
fig, ax = plt.subplots(figsize=(12, 8))
plot_regress_exog(model, "Feature1", fig=fig)
plt.show()  

# Q-Q plot
qqplot(model.resid, line="s")
plt.show()