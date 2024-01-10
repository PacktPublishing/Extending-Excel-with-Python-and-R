import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import LSTM, Dense
from sklearn.preprocessing import MinMaxScaler

# Load the time series data (replace with your data)
time_series_data = pd.read_excel('time_series_data.xlsx')

# Normalize the data to be in the range [0, 1]
scaler = MinMaxScaler()
data = scaler.fit_transform(time_series_data['Value'].to_numpy().reshape(-1, 1))

# Split the data into training and testing sets
train_size = int(len(data) * 0.67)
train, test = data[0:train_size, :], data[train_size:len(data), :]

# Create sequences and labels for training
def create_dataset(dataset, look_back=1):
    X, Y = [], []
    for i in range(len(dataset) - look_back):
        a = dataset[i:(i + look_back), 0]
        X.append(a)
        Y.append(dataset[i + look_back, 0])
    return np.array(X), np.array(Y)

look_back = 3
X_train, Y_train = create_dataset(train, look_back)
X_test, Y_test = create_dataset(test, look_back)

# Reshape the data for LSTM input
X_train = np.reshape(X_train, (X_train.shape[0], 1, X_train.shape[1]))
X_test = np.reshape(X_test, (X_test.shape[0], 1, X_test.shape[1]))

# Create and train an LSTM model
model = Sequential()
model.add(LSTM(4, input_shape=(1, look_back)))
model.add(Dense(1))
model.compile(loss='mean_squared_error', optimizer='adam')
model.fit(X_train, Y_train, epochs=100, batch_size=1, verbose=2)

# Make predictions:
trainPredict = model.predict(X_train)
testPredict = model.predict(X_test)

# Inverse transform the predictions to the original scale
trainPredict = scaler.inverse_transform(trainPredict)
testPredict = scaler.inverse_transform(testPredict)

# Plot the training predictions
trainPredictPlot = np.empty_like(data)
trainPredictPlot[:, :] = np.nan
trainPredictPlot[look_back:len(trainPredict) + look_back, :] = trainPredict

# Plot the test predictions
testPredictPlot = np.empty_like(data)
testPredictPlot[:, :] = np.nan
testPredictPlot[len(trainPredict) + (look_back * 2):len(data), :] = testPredict

# Plot the training data in blue
plt.plot(time_series_data['Value'], color='blue', label='Actual Data')

# Create shaded regions for the training and test data
plt.fill_between(range(len(data)), 0, trainPredictPlot, color='lightgray', label='Training Data')
plt.fill_between(range(len(data)), trainPredictPlot, testPredictPlot, color='lightcoral', label='Test Data')

# Overlay the predictions in green
plt.plot(testPredictPlot, color='green', label='Predictions')

plt.title('Time Series Analysis with LSTM')
plt.legend()
plt.show()