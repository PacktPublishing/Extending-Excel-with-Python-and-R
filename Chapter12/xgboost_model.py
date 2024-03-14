import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error

# Define the file path
file_path = "./Chapter 14/diamonds.xlsx"

# Load the dataset into a pandas DataFrame
df = pd.read_excel(file_path)

print(df) 

# Encode categorical variables
encoder = OneHotEncoder()
df_encoded = encoder.fit_transform(df[['cut', 'color', 'clarity']])

# Scale numerical features
scaler = StandardScaler()
df_scaled = scaler.fit_transform(df[['carat', 'depth', 'table', 'x', 'y', 'z']])

# Concatenate encoded categorical features with scaled numerical features
df_processed = np.concatenate((df_encoded.toarray(), df_scaled), axis=1)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(df_processed, df["price"], test_size=0.2, random_state=42)

print(X_train)

# Instantiate XGBoost regressor
xgb_reg = GradientBoostingRegressor(random_state=42)

# Train the model
xgb_reg.fit(X_train, y_train)

# Predict on the test set
y_pred = xgb_reg.predict(X_test)

# Calculate RMSE
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
print("Root Mean Squared Error:", rmse)
