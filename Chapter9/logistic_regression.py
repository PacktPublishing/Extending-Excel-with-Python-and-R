# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Step 0: Generate sample data
np.random.seed(0)
n_samples = 100
X = np.random.rand(n_samples, 2)  # Two features
y = (X[:, 0] + X[:, 1] > 1).astype(int)  # Binary classification based on a condition

# Create a pandas DataFrame
data = {'Feature1': X[:, 0], 'Feature2': X[:, 1], 'Target': y}
df = pd.DataFrame(data)

df.to_excel("logistic_regression_input.xlsx")

# Step 1: Import Excel data into a pandas DataFrame
excel_file = "logistic_regression_input.xlsx"
df = pd.read_excel(excel_file)

# Step 2: Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 3: Create and train the logistic regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Step 4: Visualization

# Visualization for binary classification
plt.scatter(X_test[y_test == 1][:, 0], X_test[y_test == 1][:, 1], color='blue', label='Class 1 (Actual)')
plt.scatter(X_test[y_test == 0][:, 0], X_test[y_test == 0][:, 1], color='red', label='Class 0 (Actual)')
plt.xlabel('Feature1')
plt.ylabel('Feature2')
plt.title('Logistic Regression Prediction')
plt.legend()
plt.show()

# Step 5: Model Evaluation and Interpretation
y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
class_report = classification_report(y_test, y_pred)

print("Accuracy:", accuracy)
print("Confusion Matrix:\n", conf_matrix)
print("Classification Report:\n", class_report)
